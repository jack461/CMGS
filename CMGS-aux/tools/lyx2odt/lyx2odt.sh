#!/bin/bash
# Convert the Game Master manual (LyX) to LibreOffice (ODT).
#   lyx2odt.sh /path/to/GameMaster-Doc-1.7.0.lyx
# Output : same folder, same name, .odt. Work files in a temporary folder.
set -e
LYX="$1"; HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$(cd "$(dirname "$LYX")" && pwd)"; BASE="$(basename "$LYX" .lyx)"
W="$(mktemp -d)"; echo "work folder: $W"
python3 -I - "$LYX" "$W/doc.lyx" <<'PY'
import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
t = t.replace('\\inputencoding iso8859-1', '\\inputencoding utf8')
t = t.replace('\\usepackage[latin1]{inputenc}\n', '').replace('\\include{scheme-aux}\n', '')
t = re.sub(r'(filename PIX/\S*)\.tiff?\n', r'\1.png\n', t)
open(sys.argv[2], 'w', encoding='utf-8').write(t)
PY
mkdir -p "$W/PIX"; cp "$SRC"/PIX/* "$W/PIX/"
for f in "$W"/PIX/*.tif "$W"/PIX/*.tiff; do [ -f "$f" ] && sips -s format png "$f" --out "${f%.*}.png" >/dev/null; done
/Applications/LyX.app/Contents/MacOS/lyx -batch -e pdflatex "$W/doc.lyx"
mkdir -p "$W/m"; python3 -I "$HERE/prep_tex.py" "$W/doc.tex" "$W/m/doc.tex"
ln -sf ../PIX "$W/m/PIX"; cp "$HERE/build.mk4" "$W/m/"
(cd "$W/m" && make4ht -l -u -e build.mk4 -f odt doc.tex "mathml" > make4ht.log 2>&1)
python3 -I "$HERE/odt_fix.py" "$W/m/doc.odt" "$SRC/$BASE.odt" "$W/m/doc.tex"
echo "done: $SRC/$BASE.odt"
