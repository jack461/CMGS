"""Part IV of the general manual (the list of the errors), from CMGS-Erreurs.tsv.

  python3 -I CMGS-aux/tools/md2odt/make_errors_md.py

Reads CMGS-Erreurs-intro.md (the text before the lists) and CMGS-data/CMGS-Erreurs.tsv (code <TAB> application <TAB>
explanation ; in CMGS-data since 2026-11-19 : the mSL Console reads it at run time, "? n"), writes CMGS-Manuel-P4.md : the intro, then one table per range of codes. The widths of the columns
(8 / 22 / 70 %) come from the dashes of the separator line (pandoc pipe tables, long lines). Then build the part and
insert it into the manual (insert_part.py "Partie IV —"), see the head of insert_part.py.
"""
import os
T = os.path.dirname(os.path.abspath(__file__)) + '/'
E = os.path.normpath(T + '../../../CMGS-data/CMGS-Erreurs.tsv')
rows = [l.rstrip('\n').split('\t') for l in open(E, encoding='utf-8') if l.strip()]
rows.sort(key=lambda r: int(r[0]))

def cell(t):
    t = t.replace('`set(`pval, …)`', '`` set(`pval, …) ``').replace('`thread(`new, …)`', '`` thread(`new, …) ``')
    return t.replace('|', '\\|')

secs = [(100, 999, 'Codes 0100 à 0999'), (1000, 1999, 'Codes 1000 à 1999'), (2000, 2999, 'Codes 2000 à 2999'),
        (3000, 4999, 'Codes 3000 à 4999'), (5000, 9999, 'Codes 6000 à 9999')]
out = [open(T + 'CMGS-Erreurs-intro.md', encoding='utf-8').read()]
for a, b, t in secs:
    rs = [r for r in rows if a <= int(r[0]) <= b]
    if not rs: continue
    out.append('\n## %s\n\n| Code | Application | Signification |\n|%s|%s|%s|\n' % (t, '-' * 8, '-' * 22, '-' * 70))
    out += ['| %s | %s | %s |\n' % (r[0], cell(r[1]), cell(r[2])) for r in rs]
open(T + 'CMGS-Manuel-P4.md', 'w', encoding='utf-8').write(''.join(out))
print('%d codes' % len(rows))
