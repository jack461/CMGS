"""Put LibreOffice alphabetical index marks where the LaTeX \\index{} entries were.

  python3 index_marks.py doc.idx in.odt out.odt

doc.idx comes from the TeX4ht conversion : "\\beforeentry{doc.4oo}{dx1-3001}{}" then "\\indexentry{term}{page}";
the ODT keeps a bookmark named dx1-3001 at the place of each entry. A mark is inserted just after it.
makeindex syntax : levels separated by "!", "sort@display" (the display text is kept, without its LaTeX formatting).
"""
import re, sys, zipfile
from xml.sax.saxutils import quoteattr

idxfile, src, dst = sys.argv[1:4]


def split_unquoted(s, ch):
    parts, cur, i = [], '', 0
    while i < len(s):
        c = s[i]
        if c == '"' and i + 1 < len(s):      # makeindex quote character
            cur += s[i + 1]
            i += 2
            continue
        if c == ch:
            parts.append(cur)
            cur = ''
        else:
            cur += c
        i += 1
    parts.append(cur)
    return parts


def plain(tex):
    t = tex
    t = re.sub(r'\\(texttt|emph|textbf|textit|textsf|textsc|textrm|mbox|text)\s*', '', t)
    t = t.replace('\\_', '_').replace('\\&', '&').replace('\\%', '%').replace('\\#', '#').replace('\\$', '$')
    t = t.replace('\\{', '\x01').replace('\\}', '\x02')
    t = re.sub(r'\\textbackslash\s*', '\\\\', t)
    t = re.sub(r"\\'\{?e\}?", 'é', t)
    t = re.sub(r'\\[a-zA-Z]+\s*', '', t)          # other commands
    t = t.replace('{', '').replace('}', '').replace('~', ' ')
    t = t.replace('\x01', '{').replace('\x02', '}')
    return re.sub(r'\s+', ' ', t).strip()


def levels(entry):
    out = []
    for lv in split_unquoted(entry, '!'):
        parts = split_unquoted(lv, '@') if '@' in lv else [lv]
        out.append(plain(parts[-1]))
    return [x for x in out if x]


raw = open(idxfile, encoding='utf-8', errors='replace').read()
entries = re.findall(r'\\beforeentry\{[^}]*\}\{([^}]*)\}\{\}\s*\\indexentry\{(.*)\}\{[^}]*\}', raw)
marks = {}
for anchor, entry in entries:
    lv = levels(entry)[:3]
    if not lv:
        continue
    attrs = 'text:string-value=%s' % quoteattr(lv[-1])
    if len(lv) >= 2:
        attrs += ' text:key1=%s' % quoteattr(lv[0])
    if len(lv) == 3:
        attrs += ' text:key2=%s' % quoteattr(lv[1])
    marks[anchor] = '<text:alphabetical-index-mark %s/>' % attrs

z = zipfile.ZipFile(src)
infos = z.infolist()
data = {i.filename: z.read(i.filename) for i in infos}
s = data['content.xml'].decode('utf-8')
assert '<text:alphabetical-index-mark' not in s, 'the document already has index marks'
done = set()


def put(m):
    name = m.group(1)
    if name in marks and name not in done:
        done.add(name)
        return m.group(0) + marks[name]
    return m.group(0)


s = re.sub(r'<text:bookmark text:name="(dx[^"]+)"/>', put, s)
missing = [a for a in marks if a not in done]
data['content.xml'] = s.encode('utf-8')
with zipfile.ZipFile(dst, 'w') as out:
    for i in infos:
        out.writestr(i, data[i.filename], compress_type=zipfile.ZIP_STORED if i.filename == 'mimetype' else zipfile.ZIP_DEFLATED)
print('entries', len(entries), '- marks inserted', len(done), '- anchors not found', len(missing), missing[:5])
for a, e in entries[:0]:
    pass
