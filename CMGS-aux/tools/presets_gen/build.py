import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C
import p_nuee, p_glacier, p_sillons, p_reson, p_vertige

OUT = sys.argv[1]
PRESETS = [p_nuee, p_glacier, p_sillons, p_reson, p_vertige]

for p in PRESETS:
    doc = p.DOC.rstrip()
    assert doc.lstrip().startswith('/*') and '*/' not in doc
    doc = doc + '\n' + C.USAGE.rstrip() + '\n*/\n'
    text = (p.TITLE + '\n' + doc + C.SETTINGS + C.TOOLS + p.BODY1 + C.LEVELS + p.BODY2 + C.MAIN)
    text = C.expand(text, p.NAMES)
    with open(os.path.join(OUT, p.FILE), 'w', newline='\n') as f:
        f.write(text)
    print(p.FILE, len(text.splitlines()), 'lignes')
