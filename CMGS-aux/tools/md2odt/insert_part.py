"""Insert the chapters of a generated part into a manual that the author has already edited (.fodt).

  python3 insert_part.py target.fodt fragment.fodt "Partie II —" out.fodt [prefix]
  python3 insert_part.py target.fodt fragment.fodt "before:Le langage en détail" out.fodt [prefix]
  python3 insert_part.py target.fodt fragment.fodt "sub:2:Fichiers, préréglages et exports" out.fodt [prefix]

target.fodt   the manual (edited by its author : never regenerated)
fragment.fodt the new chapters, made by the same chain (pandoc --toc, layout.py, LibreOffice export to .fodt)
"Partie II —" the beginning of the text of the paragraph of style "part" after which the chapters go ; all that
              follows it, up to the next "part" paragraph (or the end of the text), is REPLACED by the chapters of
              the fragment (everything from its first chapter heading to the end of its text). Make it unambiguous
              ("Partie II" also matches "Partie III").
"before:T"    the chapters of the fragment are INSERTED before the chapter heading (level 1) whose text is T ;
              nothing is replaced.
"sub:N:T"     (2026-11-19) sections or subsections : the fragment, from its first heading of level N to the end of
              its text, is INSERTED before the heading (of any level) whose text is T ; nothing is replaced. The
              fragment starts with the headings of its context (a chapter "# ...", a section "## ..." for
              subsections), which are not taken.
prefix        added to the names of the automatic styles of the fragment (default "x2_"), to keep them apart.

The named styles and fonts used by the fragment must exist in the target (reported if not). Update the table of
contents afterwards (lo_export2.py).
"""
import re, sys

tgt_path, frg_path, part, out_path = sys.argv[1:5]
prefix = sys.argv[5] if len(sys.argv) > 5 else 'x2_'
tgt = open(tgt_path, encoding='utf-8').read()
frg = open(frg_path, encoding='utf-8').read()


def office_text(doc):
    a = doc.index('<office:text')
    a = doc.index('>', a) + 1
    b = doc.index('</office:text>')
    return a, b


# ---- the chapters of the fragment : from the first level-1 heading to the end of its text
fa, fb = office_text(frg)
fbody = frg[fa:fb]
flevel = part.split(':')[1] if part.startswith('sub:') else '1'
m = re.search(r'<text:h\b[^>]*text:outline-level="%s"' % flevel, fbody)
assert m, 'no heading of level %s in the fragment' % flevel
chapters = fbody[m.start():].rstrip()

# ---- the automatic styles of the fragment that the chapters use (renamed)
fauto = re.search(r'<office:automatic-styles>(.*?)</office:automatic-styles>', frg, re.S).group(1)
defs = {}
for mm in re.finditer(r'<(style:style|text:list-style)\b[^>]*style:name="([^"]+)"[^>]*?(?:/>|>.*?</\1>)', fauto, re.S):
    defs[mm.group(2)] = mm.group(0)
attr = r'((?:text|table|style|draw):(?:style-name|list-style-name|parent-style-name|data-style-name|cond-style-name)=")([^"]+)(")'
used, todo = set(), set(re.findall(attr, chapters) and [x[1] for x in re.findall(attr, chapters)])
while todo:                      # styles used by the chapters, and by these styles (list styles of paragraphs...)
    n = todo.pop()
    if n in used or n not in defs:
        continue
    used.add(n)
    todo |= {x[1] for x in re.findall(attr, defs[n])}
ren = {n: prefix + n for n in used}


def rename(s):
    return re.sub(attr, lambda x: x.group(1) + ren.get(x.group(2), x.group(2)) + x.group(3), s)


chapters = rename(chapters)
new_defs = ''.join(re.sub(r'(style:name=")([^"]+)(")', lambda x: x.group(1) + ren.get(x.group(2), x.group(2)) + x.group(3),
                          rename(defs[n]), count=1) for n in sorted(used))

# ---- checks : named styles and fonts used by the fragment
tstyles = set(re.findall(r'style:name="([^"]+)"', tgt))
named = {x[1] for x in re.findall(attr, chapters + new_defs)} - set(ren.values())
missing = sorted(n for n in named if n not in tstyles)
# a named style that the target lacks (e.g. "Graphics", for the first image of a manual) is copied from the
# office:styles of the fragment, when it is defined there
fstyles = re.search(r'<office:styles>(.*?)</office:styles>', frg, re.S).group(1)
copied = []
for n in list(missing):
    mm = re.search(r'<style:style\b[^>]*style:name="%s"[^>]*?(?:/>|>.*?</style:style>)' % re.escape(n), fstyles, re.S)
    if mm:
        tgt = tgt.replace('</office:styles>', mm.group(0) + '</office:styles>', 1)
        copied.append(n)
        missing.remove(n)
if copied:
    print('named styles copied from the fragment:', copied)
tfonts = set(re.findall(r'<style:font-face style:name="([^"]+)"', tgt))
ffonts = set(re.findall(r'style:font-name(?:-asian|-complex)?="([^"]+)"', new_defs))
missing_fonts = sorted(f for f in ffonts if f not in tfonts)
if missing or missing_fonts:
    print('MISSING named styles:', missing, ' fonts:', missing_fonts)
    sys.exit(1)

ta, tb = office_text(tgt)
tbody = tgt[ta:tb]
if part.startswith('sub:'):
    # ---- insert sections (or subsections) before a heading of any level
    title = ' '.join(part.split(':', 2)[2].split())
    heads = [mm for mm in re.finditer(r'<text:h\b[^>]*>(.*?)</text:h>', tbody, re.S)
             if ' '.join(re.sub(r'<[^>]+>', '', mm.group(1)).split()) == title]
    assert len(heads) == 1, 'heading not found (or found twice): ' + title
    start = end = heads[0].start()
elif part.startswith('before:'):
    # ---- insert the chapters before a chapter heading
    title = ' '.join(part[len('before:'):].split())
    heads = [mm for mm in re.finditer(r'<text:h\b[^>]*text:outline-level="1"[^>]*>(.*?)</text:h>', tbody, re.S)
             if ' '.join(re.sub(r'<[^>]+>', '', mm.group(1)).split()) == title]
    assert len(heads) == 1, 'chapter heading not found (or found twice): ' + title
    start = end = heads[0].start()
else:
    # ---- replace the chapters after the "part" paragraph
    parts = [mm for mm in re.finditer(r'<text:p\b[^>]*text:style-name="part"[^>]*>(.*?)</text:p>', tbody, re.S)]
    idx = [i for i, mm in enumerate(parts) if re.sub(r'<[^>]+>', '', mm.group(1)).strip().startswith(part)]
    assert len(idx) == 1, 'part paragraph not found (or found twice): ' + part
    i = idx[0]
    start = parts[i].end()
    end = parts[i + 1].start() if i + 1 < len(parts) else len(tbody.rstrip())
old = tbody[start:end]
print('replaced : %d characters, %d chapter(s) ; inserted : %d chapter(s), %d heading(s), %d automatic styles'
      % (len(old), len(re.findall(r'text:outline-level="1"', old)), len(re.findall(r'text:outline-level="1"', chapters)),
         len(re.findall(r'<text:h\b', chapters)), len(used)))
tbody = tbody[:start] + '\n' + chapters + '\n' + tbody[end:]
out = tgt[:ta] + tbody + tgt[tb:]
out = out.replace('</office:automatic-styles>', new_defs + '</office:automatic-styles>', 1)

import xml.dom.minidom as dm
dm.parseString(out.encode('utf-8'))
open(out_path, 'w', encoding='utf-8').write(out)
print('ok')
