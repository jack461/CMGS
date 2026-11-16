#!/usr/bin/env python3
"""Builds the self-contained CMGS-auxiliary.eel of the root of the CMGS repository.

    python3 -I CMGS-aux/tools/make_auxiliary.py            rebuild CMGS-auxiliary.eel
    python3 -I CMGS-aux/tools/make_auxiliary.py --check    exit 1 if CMGS-auxiliary.eel is not up to date

The source is CMGS-effects/CMGS-libs/CMGS-auxiliary-src.eel : it includes (preprocessor lines
<? include("X.jsfx-inc"); ?>) files of CMGS-libs, such as the gmem table mSL_gmem_map.jsfx-inc, that it must
follow. The users copy CMGS-auxiliary.eel alone into REAPER/Scripts, where these includes would not be found :
this tool copies the included files in place of the include lines. The included files must not include others.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CMGS = os.path.dirname(os.path.dirname(HERE))          # the CMGS repository (this file is in CMGS-aux/tools)
LIBS = os.path.join(CMGS, 'CMGS-effects', 'CMGS-libs')
SRC = os.path.join(LIBS, 'CMGS-auxiliary-src.eel')
DEST = os.path.join(CMGS, 'CMGS-auxiliary.eel')
INCLUDE = re.compile(r'^\s*<\?\s*include\("([^"]+)"\);\s*\?>\s*$')


def build():
    out = ['// ' + '=' * 110,
           '// GENERATED FILE : do not edit. Source : CMGS-effects/CMGS-libs/CMGS-auxiliary-src.eel',
           '// (with its includes copied in place), built by : python3 -I CMGS-aux/tools/make_auxiliary.py',
           '// Copy this file into REAPER/Scripts, then load it as an action (Actions > New action > Load ReaScript...).',
           '// ' + '=' * 110, '']
    for line in open(SRC, encoding='utf-8').read().split('\n'):
        m = INCLUDE.match(line)
        if not m:
            out.append(line)
            continue
        name = m.group(1)
        path = os.path.join(LIBS, name)
        text = open(path, encoding='utf-8').read()
        if re.search(r'<\?\s*include\(', text):
            sys.exit(f'make_auxiliary: {name} includes another file : not supported')
        out.append(f'// ---------- begin of {name} (copied from CMGS-libs) ----------')
        out.extend(text.rstrip('\n').split('\n'))
        out.append(f'// ---------- end of {name} ----------')
    return '\n'.join(out)


def main():
    text = build()
    old = open(DEST, encoding='utf-8').read() if os.path.exists(DEST) else None
    if '--check' in sys.argv[1:]:
        if old == text:
            print('CMGS-auxiliary.eel is up to date')
            return 0
        print('CMGS-auxiliary.eel is NOT up to date : run python3 -I CMGS-aux/tools/make_auxiliary.py')
        return 1
    if old == text:
        print('CMGS-auxiliary.eel unchanged')
    else:
        with open(DEST, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'CMGS-auxiliary.eel written ({text.count(chr(10)) + 1} lines)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
