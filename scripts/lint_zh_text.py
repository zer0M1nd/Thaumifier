#!/usr/bin/env python3
"""lint_zh_text.py — 魔导手册中文文本风格 / 格式检查器（只依赖 Python 3 标准库）

三种用法：

1) 比较改写前后的两个语言文件（JSON 或 .lang），只检查值发生变化的键：
     python3 lint_zh_text.py --before old/zh_cn.json --after new/zh_cn.json

2) 检查一个“成对”文件，可显式给出每个键的类型和页面模式：
     python3 lint_zh_text.py --pairs pairs.json
   pairs.json 格式：
     {"<key>": {"old": "改写前（可省略）", "new": "改写后",
                "kind": "title|subtitle|page（可省略，按键名推断）",
                "legacy": true|false|null（可省略，按原文推断）}}

3) 检查单段文本：
     python3 lint_zh_text.py --text "……" [--kind page|subtitle|title] [--native]

可选参数：
     --native-keys FILE   每行一个键，强制视为原生组件页（换行只能用 \\n）
     --legacy-keys FILE   每行一个键，强制视为旧式页（可用 <BR>/<LINE>/<IMG>）
     --max-page N         单页长度警告阈值（默认 250 字）
     --json               以 JSON 输出结果

退出码：有 ERROR 时为 1，否则为 0。WARN 需要人工判断。
"""
import argparse, collections, json, re, sys

PH = re.compile(r'%(?:\d+\$)?[sdf%]')
IMG = re.compile(r'<IMG>.*?</IMG>', re.S)
TAG = re.compile(r'<([A-Za-z/]+)>')
LEGACY_TAGS = {'BR', 'BR/', 'LINE', 'IMG', '/IMG'}
SECT = re.compile(r'§(.)')
VALID_SECT = set('0123456789abcdefklmnor')
CJK = r'[一-鿿]'
HALF_PUNCT = re.compile(CJK + r'[,.;:?!]' + r'(?=' + CJK + r'|$|<|\s)')
META_WORDS = ['实现说明', '本附属', '本模组', '本移植', '移植版', '原作者', '原作', '代码', '服务端', '客户端',
              '数据包', 'JEI', '实现', '版本号', 'WIP', 'TODO', '您', '请']
NUM = re.compile(r'(?<![A-Za-z_])\d+(?:[.,]\d+)?')


def strip_markup(s):
    s = IMG.sub('', s)
    s = re.sub(r'<BR/?>|<LINE>', '', s)
    s = re.sub(r'§.', '', s)
    return s.replace('\n', '').strip()


def infer_kind(key):
    if '.research_name.' in key or key.startswith('tc.research_name'):
        return 'title'
    if '.research_text.' in key or key.startswith('tc.research_text') or '.tag.' in key or '.lore.' in key:
        return 'subtitle'
    return 'page'


def infer_legacy(old):
    if old is None:
        return None
    if re.search(r'<BR/?>|<LINE>|<IMG>', old):
        return True
    if '\n' in old:
        return False
    return None


def load_lang(path):
    if path.endswith('.json'):
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
        return {k: v for k, v in d.items() if isinstance(v, str)}
    d = {}
    with open(path, encoding='utf-8-sig', errors='replace') as f:
        for line in f:
            line = line.rstrip('\r\n')
            if '=' in line and not line.lstrip().startswith('#'):
                k, v = line.split('=', 1)
                d[k.strip()] = v
    return d


def numbers(s):
    s = IMG.sub('', s)
    s = re.sub(r'§.|%\d+\$[sd]', '', s)
    return collections.Counter(NUM.findall(s))


def lint_one(key, new, old=None, kind=None, legacy=None, title_new=None, max_page=250):
    E, W = [], []
    kind = kind or infer_kind(key)
    if legacy is None:
        legacy = infer_legacy(old)
    if not isinstance(new, str) or not new.strip():
        return ['空文本'], []
    # placeholders
    if old is not None and collections.Counter(PH.findall(old)) != collections.Counter(PH.findall(new)):
        E.append(f'占位符不一致：原 {PH.findall(old)} → 新 {PH.findall(new)}')
    # section codes
    for c in SECT.findall(new):
        if c.lower() not in VALID_SECT:
            E.append(f'无效格式码 §{c}')
        elif c.lower() == 'k':
            W.append('使用了 §k（乱码字），手册中不应使用')
        elif c.lower() == 'f':
            W.append('使用了 §f（白字），在羊皮纸底色上几乎不可见')
    if new.rstrip().endswith('§'):
        E.append('文本以孤立的 § 结尾')
    # unterminated style
    tail = new.split('§r')[-1]
    if re.search(r'§[lmno]', tail) and kind != 'page':
        W.append('样式码（§l/§m/§n/§o）之后没有 §r 结束')
    if kind in ('title', 'subtitle'):
        if re.search(r'<[A-Za-z/]+>', new) or '\n' in new:
            E.append(f'{kind} 中含有标记或换行')
        if re.search(r'§', new):
            W.append(f'{kind} 中含有格式码（原版极少如此）')
        n = len(strip_markup(new))
        if kind == 'subtitle':
            if title_new is not None and strip_markup(new) == strip_markup(title_new):
                E.append('副标题与标题相同')
            if n > 15:
                W.append(f'副标题过长（{n} 字，原版中位数 6、建议 ≤ 10、最长不宜超过 15）')
            elif n > 10:
                W.append(f'副标题偏长（{n} 字）')
            if new.rstrip().endswith('。'):
                W.append('副标题以句号结尾（原版不加句号）')
        if kind == 'title' and n > 12:
            W.append(f'标题偏长（{n} 字）')
    else:
        tags = TAG.findall(new)
        if legacy is False and any(t in LEGACY_TAGS for t in tags):
            E.append('原生组件页中出现 <BR>/<LINE>/<IMG>，换行应写作 \\n')
        for t in tags:
            if t not in LEGACY_TAGS:
                E.append(f'未知标记 <{t}>')
        if legacy is True and '\n' in new:
            W.append('旧式页中出现真实换行符（.lang 不支持；应改为 <BR>）')
        if old is not None:
            for img in IMG.findall(old):
                if img not in new:
                    E.append(f'丢失插图 {img[:60]}…')
            if len(IMG.findall(new)) > len(IMG.findall(old)):
                W.append('新增了 <IMG>，请确认图片资源存在')
            miss = numbers(old) - numbers(new)
            if miss:
                W.append(f'原文中的数字在新文本里缺失（请核对事实）：{sorted(miss)}')
            lo, ln = len(strip_markup(old)), len(strip_markup(new))
            if lo > 40 and ln < 0.7 * lo:
                W.append(f'明显变短（{ln} / 原 {lo} 字），可能丢失事实')
            if ln > 2.2 * max(lo, 60):
                W.append(f'明显变长（{ln} / 原 {lo} 字），可能注水或应拆页')
        ln = len(strip_markup(new))
        if ln > max_page:
            W.append(f'单页较长（{ln} 字；原版中位数约 100、90% ≤ 175），考虑拆页')
    # punctuation
    if HALF_PUNCT.search(strip_markup(new)):
        W.append('汉字之间出现半角标点（应使用全角，例：，。；：？！）')
    if '...' in new:
        W.append('使用了 "..."（建议用“……”）')
    # meta words
    for w in META_WORDS:
        if w in new and (old is None or w not in old or w in ('您', '请')):
            if w == '原作' and ('原作者' in new):
                continue
            W.append(f'出现元信息 / 敬语词“{w}”（若必须保留，请改为括号旁白）')
    return E, W


def batch_checks(items):
    """跨条目检查：泛化共用副标题、开头套路。items: list of (key, kind, new)"""
    W = []
    subs = collections.defaultdict(list)
    for k, kind, new in items:
        if kind == 'subtitle':
            subs[strip_markup(new)].append(k)
    for s, ks in subs.items():
        if len(ks) >= 3:
            W.append(f'{len(ks)} 个研究共用副标题“{s}”——只有真正平行的系列才可共用：{ks[:6]}{"…" if len(ks) > 6 else ""}')
    pages = [strip_markup(new) for k, kind, new in items if kind == 'page']
    if len(pages) >= 10:
        heads = collections.Counter(p[:2] for p in pages if p)
        for h, c in heads.most_common(3):
            if c / len(pages) >= 0.2:
                W.append(f'套路疲劳：{c}/{len(pages)} 页以“{h}”开头')
    return W


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--before'); ap.add_argument('--after'); ap.add_argument('--pairs')
    ap.add_argument('--text'); ap.add_argument('--kind', choices=['page', 'subtitle', 'title'])
    ap.add_argument('--native', action='store_true'); ap.add_argument('--native-keys'); ap.add_argument('--legacy-keys')
    ap.add_argument('--max-page', type=int, default=250); ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    force = {}
    for path, val in ((a.native_keys, False), (a.legacy_keys, True)):
        if path:
            for line in open(path, encoding='utf-8'):
                if line.strip():
                    force[line.strip()] = val
    entries = []  # key, new, old, kind, legacy
    fullnew = {}
    if a.text is not None:
        entries.append(('(text)', a.text, None, a.kind or 'page', False if a.native else None))
    elif a.pairs:
        d = json.load(open(a.pairs, encoding='utf-8'))
        for k, v in d.items():
            if isinstance(v, str):
                v = {'new': v}
            entries.append((k, v['new'], v.get('old'), v.get('kind'), v.get('legacy')))
    elif a.before and a.after:
        old, new = load_lang(a.before), load_lang(a.after)
        fullnew = new
        for k, v in new.items():
            if k in old and old[k] != v:
                entries.append((k, v, old[k], None, None))
            elif k not in old:
                entries.append((k, v, None, None, None))
        missing = [k for k in old if k not in new]
        if missing:
            print(f'ERROR 改写后文件缺少 {len(missing)} 个键：{missing[:10]}')
    else:
        ap.print_help(); sys.exit(2)
    newmap = dict(fullnew)
    newmap.update({k: n for k, n, *_ in entries})
    results, n_err, n_warn, batch = [], 0, 0, []
    for k, n, o, kind, leg in entries:
        kind = kind or infer_kind(k)
        if k in force:
            leg = force[k]
        title_new = None
        if kind == 'subtitle':
            for a1, b1 in (('.research_text.', '.research_name.'), ('.tag.', '.name.'), ('.lore.', '.name.')):
                if a1 in k:
                    tk = k.replace(a1, b1)
                    title_new = newmap.get(tk)
        E, W = lint_one(k, n, o, kind, leg, title_new, a.max_page)
        n_err += len(E); n_warn += len(W)
        results.append({'key': k, 'kind': kind, 'errors': E, 'warnings': W})
        batch.append((k, kind, n))
    BW = batch_checks(batch)
    n_warn += len(BW)
    if a.json:
        print(json.dumps({'results': results, 'batch_warnings': BW, 'errors': n_err, 'warnings': n_warn}, ensure_ascii=False, indent=1))
    else:
        for r in results:
            for e in r['errors']:
                print(f"ERROR [{r['key']}] {e}")
        for r in results:
            for w in r['warnings']:
                print(f"WARN  [{r['key']}] {w}")
        for w in BW:
            print(f'WARN  [批量] {w}')
        print(f'— 共检查 {len(results)} 条：{n_err} 个 ERROR，{n_warn} 个 WARN')
    sys.exit(1 if n_err else 0)


if __name__ == '__main__':
    main()
