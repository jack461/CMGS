"""Prepare the LaTeX exported by LyX (pdflatex flavour) for make4ht (LuaLaTeX, ODT output).

  python3 prep_tex.py doc.tex out.tex
"""
import re, sys

t = open(sys.argv[1], encoding='utf-8').read()


def rep(old, new, count=1):
    global t
    n = t.count(old)
    assert n >= 1, 'not found: %r' % old[:60]
    t = t.replace(old, new) if count == 0 else t.replace(old, new, count)


# --- Preamble -------------------------------------------------------------
rep('\\usepackage[LGR,T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n', '\\usepackage{fontspec}\n')
for line in ('\\usepackage[T1]{fontenc}\n', '\\usepackage{times}\n', '\\usepackage{mathptm}\n',
             '\\pdfpageheight\\paperheight\n', '\\pdfpagewidth\\paperwidth\n',
             '\\addtolength{\\hoffset}{-0.25cm}\n\\addtolength{\\textwidth}{0.50cm}\n',
             '\\pagestyle{headings}\n\\usepackage{babel}\n'):
    if line in t:
        t = t.replace(line, '')
# babel-french redefines \part in a way TeX4ht does not support
rep('\\usepackage{babel}\n', '\\usepackage{babel}\n\\frenchsetup{PartNameFull=false}\n')
# French active characters break TeX4ht's internal names; \vref would print TeX4ht page numbers
rep('\\makeatother\n\n\\begin{document}',
    '\\AtBeginDocument{\\shorthandoff{:;!?}\\let\\vref\\ref\\let\\vpageref\\relax}\n\\makeatother\n\n\\begin{document}')
# LyX menu arrows : text characters instead of formulas
rep('{\\leavevmode\\,$\\triangleleft$\\,\\allowbreak}', '{\\leavevmode\\,◁\\,\\allowbreak}')
rep('{\\leavevmode\\,$\\triangleright$\\,\\allowbreak}', '{\\leavevmode\\,▷\\,\\allowbreak}')

# --- Body -------------------------------------------------------------------
# title page alone on page 1
rep('\\vfill \\eject Document de travail.', '\\vfill \\eject \\newpage Document de travail.')
# "Table des Matières" listed inside the table of contents itself
rep('\\addcontentsline{toc}{section}{Table des Mati{\\`e}res}', '')
# no index in the ODT (it would refer to TeX4ht page numbers)
t = t.replace('\\printindex{}', '').replace('\\printindex', '')

# Symbols written as formulas : Unicode text
SYMBOLS = {
    '\\searrow': '↘', '\\nwarrow': '↖', '\\bowtie': '⋈',
    '\\blacktriangleleft': '◀', '\\blacktriangleright': '▶',
    '\\blacktriangle': '▲', '\\blacktriangledown': '▼',
    '\\Uparrow': '⇑', '\\Downarrow': '⇓',
}
for cmd, ch in SYMBOLS.items():
    t = t.replace('$' + cmd + '$', ch)
t = t.replace('$\\left[0.6\\;1.1\\right]$', '[0.6 1.1]')


# \index{} inside section titles makes TeX4ht loop : move them after the title
def braced(s, i):
    d = 0
    for j in range(i, len(s)):
        c = s[j]
        if c == '{' and s[j - 1] != '\\':
            d += 1
        elif c == '}' and s[j - 1] != '\\':
            d -= 1
            if d == 0:
                return j + 1
    return -1


out, pos = [], 0
for m in re.finditer(r'\\(part|chapter|section|subsection|subsubsection|paragraph|subparagraph)\*?(\[[^\]]*\])?\{', t):
    if m.start() < pos:
        continue
    s = m.end() - 1
    e = braced(t, s)
    title = t[s:e]
    idx, new, k = [], '', 0
    while True:
        i = title.find('\\index{', k)
        if i < 0:
            new += title[k:]
            break
        ee = braced(title, i + 6)
        idx.append(title[i:ee])
        new += title[k:i]
        k = ee
    if idx:
        out.append(t[pos:s])
        out.append(new + ''.join(idx))
        pos = e
out.append(t[pos:])
t = ''.join(out)

open(sys.argv[2], 'w', encoding='utf-8').write(t)
