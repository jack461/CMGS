"""Inventory of the error codes of CMGS : code -> applications, places, messages, comments.

  python3 -I CMGS-aux/tools/errors_extract.py out.json [old_manual.txt]

Scans CMGS-effects (block comments skipped, dispatch tables "Err=N" between //===N===// ignored) for the error codes
(xxErr = NNNN, xx_err(NNNN, ...), "ERR: NNNN", ternaries on an error assignment). Then compare with the list of the
general manual, CMGS-aux/tools/md2odt/CMGS-Erreurs.tsv (code, application, explanation), to find the new codes :
  python3 -I -c "import json;e={o['code'] for o in json.load(open('out.json')) if o['in_code']};
t={l.split()[0] for l in open('CMGS-aux/tools/md2odt/CMGS-Erreurs.tsv')};print(sorted(e-t), sorted(t-e))"
old_manual.txt (optional) : the text of the old Game Master manual (made by fodt2txt.py), to get its texts of ch. 18.
"""
import re, glob, os, json, sys
BASE = '/Users/jjg4/CMGS-FULL/CMGS/'
files = sorted(glob.glob(BASE + 'CMGS-effects/CMGS-libs/*.jsfx-inc') + glob.glob(BASE + 'CMGS-effects/*.jsfx')
               + [BASE + 'CMGS-effects/CMGS-libs/CMGS-auxiliary-src.eel'])
skip = ('The_Obsolete', 'unused.jsfx', 'ZZZ', 'string_list', 'Vars_Access')
files = [f for f in files if not any(s in f for s in skip)]
def app(f):
    b = os.path.basename(f)
    for k, v in (('GamePlayer', 'Game Master'), ('mSL_clip_lib', 'Game Master'), ('FilePlayer', 'FilePlayer'),
                 ('ScriptMaster', 'ScriptMaster'), ('Diffusion-3', 'Diffusion-3'), ('AKAI-APCmini', 'Diffusion-3'),
                 ('Interstys', 'Interstys'), ('MIDI', 'MIDI_In'), ('CMGS-auxiliary', 'script auxiliaire'),
                 ('MCBM', 'MCBM'), ('SmoothMultiLimiter', 'SmoothMultiLimiter')):
        if k in b: return v
    return 'commun'
# error contexts
pats = [
  re.compile(r'\b(\w*[Ee]rr\w*)\s*=\s*(-?\d{3,4})\b(?![.\d])'),                 # xxErr = 1234
  re.compile(r'\b(\w*[Ee]rr\w*)\s*\(\s*(-?\d{3,4})\b(?![.\d])'),                # xx_err(1234, ...)
  re.compile(r'"(?:\*\*\* )?ERR:? *(\d{3,4})\b'),                                # "ERR: 1234 ..."
  re.compile(r'\b(error)\s*\(\s*(\d{3,4})\b'),
]
inv = {}
for f in files:
    raw = open(f, encoding='utf-8', errors='replace').read()
    # blank the block comments /* ... */ (dead code), keeping the lines ; strings and // comments are respected
    out_c, i_, n_, st = [], 0, len(raw), 0
    while i_ < n_:
        ch = raw[i_]
        if st == 0:
            if ch == '"': st = 1
            elif raw.startswith('//', i_): st = 2
            elif raw.startswith('/*', i_): st = 3; out_c.append('  '); i_ += 2; continue
            out_c.append(ch)
        elif st == 1:
            out_c.append(ch)
            if ch == '"' or ch == '\n': st = 0
        elif st == 2:
            out_c.append(ch)
            if ch == '\n': st = 0
        else:
            if raw.startswith('*/', i_): st = 0; out_c.append('  '); i_ += 2; continue
            out_c.append('\n' if ch == '\n' else ' ')
        i_ += 1
    lines = ''.join(out_c).split('\n')
    for i, l in enumerate(lines):
        code_part = l.split('//')[0] if not l.lstrip().startswith('"') else l
        found = set()
        for p in pats:
            for m in p.finditer(l):
                g = m.groups(); c = int(g[-1])
                if c < 0: c = -c
                if c < 100 and not ('ERR' in m.group(0)): continue
                found.add(c)
        # ternary forms on a line that assigns an error variable : xxErr = (cond ? 0503 : 0504)
        if re.search(r'\b\w*[Ee]rr\w*\s*=(?!=)', l):
            for m in re.finditer(r'[?:]\s*\(?\s*(\d{3,4})\b(?![.\d])', l.split('//')[0]):
                c = int(m.group(1))
                if c >= 100: found.add(c)
        # dispatch tables : "Err=N" between the markers //===N===// (unknown command N) : not an error code
        prevl = lines[i-1] if i else ''
        mk = re.search(r'//[=:—-]+(\d+)[=:+—-]+//', prevl)
        if mk and int(mk.group(1)) in found and re.match(r'\s*\w*[Ee]rr\w*\s*=\s*\d+\s*;\s*$', l):
            found.discard(int(mk.group(1)))
        for c in found:
            # message : strings on the line and the next 2 lines ; comment on the line
            ctx = ' '.join(lines[i:i+3])
            msgs = [s for s in re.findall(r'"([^"]{6,})"', ctx) if not s.startswith('%') or ' ' in s]
            com = l.split('//', 1)[1].strip() if '//' in l else ''
            prev = lines[i-1].strip() if i else ''
            e = inv.setdefault(c, {'apps': set(), 'where': [], 'msgs': [], 'coms': [], 'line': '', 'func': ''})
            if not e['line']:
                e['line'] = ' '.join(x.strip() for x in lines[max(0,i-1):i+2])[:220]
                j = i
                while j > 0 and not re.match(r'\s*function\s+\w+|^\w+\s*\(.*\)\s*$', lines[j]): j -= 1
                e['func'] = (lines[j].strip()[:60] if j > 0 else '')
            e['apps'].add(app(f)); e['where'].append('%s:%d' % (os.path.basename(f), i+1))
            for s in msgs:
                if s not in e['msgs']: e['msgs'].append(s)
            for s in (com, prev if prev.startswith('//') else ''):
                if s and s not in e['coms']: e['coms'].append(s[:160])
# manual ch. 18
man = open(sys.argv[2], encoding='utf-8').read().split('\n') if len(sys.argv) > 2 else ['# 18 ', '# 19 ']
s0 = next(i for i, l in enumerate(man) if l.startswith('# 18 '))
s1 = next(i for i, l in enumerate(man) if l.startswith('# 19 '))
mt = {}
k = s0 + 1
while k < s1:
    l = man[k].strip()
    m = re.match(r'^(\d{4})((?:\s*(?:,|à|-|et)\s*\d{4})*)\s*$', l)
    if m and k + 1 < s1:
        nums = [int(x) for x in re.findall(r'\d{4}', l)]
        txt = man[k+1].strip()
        if 'à' in l and len(nums) == 2 and nums[1] - nums[0] < 40:
            nums = list(range(nums[0], nums[1] + 1))
        for c in nums: mt.setdefault(c, txt)
        k += 2; continue
    k += 1
out = []
for c in sorted(set(inv) | set(mt)):
    e = inv.get(c, {'apps': set(), 'where': [], 'msgs': [], 'coms': [], 'line': '', 'func': ''})
    out.append({'code': '%04d' % c, 'apps': sorted(e['apps']), 'where': e['where'][:6], 'msgs': e['msgs'][:4],
                'coms': e['coms'][:3], 'manual': mt.get(c, ''), 'in_code': c in inv, 'line': e['line'], 'func': e['func']})
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
print('codes in code:', len(inv), ' in manual:', len(mt), ' union:', len(out))
print('manual only (not found in code):', [o['code'] for o in out if not o['in_code']][:80])
from collections import Counter
print('by thousand:', sorted(Counter(int(o['code'])//1000 for o in out if o['in_code']).items()))
print('by app:', Counter(a for o in out for a in o['apps']).most_common())
