"""Non-breaking spaces in an ODT (French typography), code left unchanged.

  python3 nbsp.py in.odt out.odt

- a space after "«" and before a non blank character
- a space after a non blank character and before "»", ";", "?", ":" or "!"
become U+00A0. Text in monospace styles (code) is not modified.
"""
import re, sys, zipfile, collections

src, dst = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)
infos = z.infolist()
data = {i.filename: z.read(i.filename) for i in infos}
s = data['content.xml'].decode('utf-8')
st = data['styles.xml'].decode('utf-8')

# monospace styles (text and paragraph), in content.xml and styles.xml
mono_fonts = set()
for x in (s, st):
    for m in re.finditer(r'<style:font-face style:name="([^"]*)"[^>]*svg:font-family="([^"]*)"', x):
        if re.search(r'mono|courier|lmtt', m.group(2), re.I):
            mono_fonts.add(m.group(1))
mono = set()
for x in (s, st):
    for m in re.finditer(r'<style:style style:name="([^"]*)" style:family="(?:text|paragraph)"[^>]*>(.*?)</style:style>', x, re.S):
        fn = re.search(r'style:font-name="([^"]*)"', m.group(2))
        if fn and fn.group(1) in mono_fonts:
            mono.add(m.group(1))
print('monospace styles:', sorted(mono))

b = s.index('<office:body>')
body = s[b:]
tokens = re.findall(r'<[^>]+>|[^<]+', body)

BOUNDARY = re.compile(r'</?text:(p|h)\b|<text:(line-break|tab)\b|</?text:(list|list-item|table-of-content|index-body|section)\b|</?table:')
units = []          # [kind, char, token index, offset, in_code]  kind: 'c' char, 's' text:s, 'b' boundary
stack = []          # (tag name, is_mono)
for ti, tok in enumerate(tokens):
    code = any(m for _, m in stack)
    if tok.startswith('<'):
        m = re.match(r'<(/?)([\w:-]+)([^>]*?)(/?)>', tok)
        closing, name, attrs, selfclose = m.group(1), m.group(2), m.group(3), m.group(4)
        if name == 'text:s':
            c = re.search(r'text:c="(\d+)"', attrs)
            units.append(['s' if not c or c.group(1) == '1' else 'b', ' ', ti, 0, code])
        elif BOUNDARY.match(tok):
            units.append(['b', '', ti, 0, code])
        # a formula/image in the text or a footnote call : a visible (non blank) item
        if (name == 'draw:frame') or (name == 'text:note' and closing):
            units.append(['c', 'X', ti, -2, code])
        if name in ('text:span', 'text:p', 'text:h'):
            if closing:
                if stack and stack[-1][0] == name:
                    stack.pop()
            elif not selfclose:
                sty = re.search(r'text:style-name="([^"]*)"', attrs)
                stack.append((name, bool(sty and sty.group(1) in mono)))
    else:
        for mm in re.finditer(r'&[^;]+;|.', tok, re.S):
            ch = mm.group(0)
            units.append(['c', ch, ti, mm.start(), code])

def blank(u):
    return u[0] == 'b' or (u[0] in 'cs' and u[1] in (' ', '\n', '\t', ' '))

changes = collections.Counter()
samples = []
repl = {}  # (token index, offset) -> new ; offset -1 for text:s token
for i in range(1, len(units) - 1):
    u = units[i]
    if u[4] or not (u[0] == 's' or (u[0] == 'c' and u[1] == ' ')):
        continue
    p, n = units[i - 1], units[i + 1]
    rule = None
    if p[0] == 'c' and p[1] == '«' and not blank(n):
        rule = '«'
    elif not blank(p) and n[0] == 'c' and n[1] in ('»', ';', '?', ':', '!'):
        rule = n[1]
    if rule:
        changes[rule] += 1
        repl[(u[2], u[3] if u[0] == 'c' else -1)] = True
        if len(samples) < 12:
            ctx = ''.join(x[1] for x in units[max(0, i - 12):i + 12] if x[0] != 'b')
            samples.append(ctx.replace(' ', '·'))

# apply
by_tok = collections.defaultdict(list)
for (ti, off) in repl:
    by_tok[ti].append(off)
for ti, offs in by_tok.items():
    if offs == [-1]:
        tokens[ti] = ' '
    else:
        t = list(tokens[ti])
        for off in offs:
            assert t[off] == ' '
            t[off] = ' '
        tokens[ti] = ''.join(t)
s = s[:b] + ''.join(tokens)
data['content.xml'] = s.encode('utf-8')
with zipfile.ZipFile(dst, 'w') as out:
    for i in infos:
        out.writestr(i, data[i.filename], compress_type=zipfile.ZIP_STORED if i.filename == 'mimetype' else zipfile.ZIP_DEFLATED)
print('changes:', dict(changes), 'total', sum(changes.values()))
for x in samples:
    print('   ', x)
