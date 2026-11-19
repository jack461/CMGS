"""Copy the refreshed index bodies (table of contents, alphabetical index...) of a LibreOffice re-save into the
edited .fodt.

  python3 -I copy_index.py edited.fodt lo_output.fodt out.fodt

A headless LibreOffice re-save (lo_export2.py) updates the indexes and the page numbers, but drops the author's view
settings and reorders bookmarks. So the edited file is kept, and only the <text:index-body> of each index is taken
from the re-save (same indexes, in the same order, in both files).
"""
import re, sys

ed_path, lo_path, out_path = sys.argv[1:4]
ed = open(ed_path, encoding='utf-8').read()
lo = open(lo_path, encoding='utf-8').read()
IDX = r'<text:(table-of-content|alphabetical-index|illustration-index|table-index|object-index|user-index)(?=[\s>])'
BODY = re.compile(r'<text:index-body>.*?</text:index-body>', re.S)


def bodies(doc):
    out = []
    for m in re.finditer(IDX, doc):
        b = BODY.search(doc, m.end())
        out.append((m.group(1), b.start(), b.end()))
    return out


eb, lb = bodies(ed), bodies(lo)
assert [k for k, _, _ in eb] == [k for k, _, _ in lb], ([k for k, _, _ in eb], [k for k, _, _ in lb])
parts, pos = [], 0
for (k, s, e), (_, ls, le) in zip(eb, lb):
    parts.append(ed[pos:s])
    parts.append(lo[ls:le])
    pos = e
parts.append(ed[pos:])
out = ''.join(parts)
assert out.count('<text:index-body>') == ed.count('<text:index-body>') == len(eb)
import xml.dom.minidom as dm
dm.parseString(out.encode('utf-8'))
open(out_path, 'w', encoding='utf-8').write(out)
print('indexes copied:', ', '.join(k for k, _, _ in eb))
