# Expand a JSFX shell (includes + _suppress parts, roughly as the preprocessor) and report the functions called before
# their first definition. Usage: python3 defcheck.py Diffusion-3.jsfx [--only file1,file2]
import re, sys, os

ROOT = os.getcwd()
var = {}
out = []  # (file, lineno, text)

def evalcond(expr):
    # "a != 1", "a == 2", "a != 0"
    m = re.match(r'\s*(\w+)\s*(!=|==)\s*(-?\d+)\s*$', expr)
    if not m:
        return None
    v = var.get(m.group(1), 0)
    n = int(m.group(3))
    return (v != n) if m.group(2) == '!=' else (v == n)

def expand(path):
    lines = open(os.path.join(ROOT, path), encoding='utf-8', errors='replace').read().split('\n')
    suppress = False
    in_pp = False
    for i, l in enumerate(lines):
        s = l.strip()
        # single-line preprocessor blocks
        for blk in re.findall(r'<\?(.*?)\?>', l):
            # assignments and includes, in order
            for stmt in [x.strip() for x in blk.split(';') if x.strip()]:
                m = re.match(r'(\w+)\s*(!=|==)\s*(-?\d+)\s*\?\s*_suppress\s*=\s*(\d)', stmt)
                if m:
                    c = evalcond('%s %s %s' % (m.group(1), m.group(2), m.group(3)))
                    if c:
                        suppress = bool(int(m.group(4)))
                    continue
                m = re.match(r'_suppress\s*=\s*(\d)', stmt)
                if m:
                    suppress = bool(int(m.group(1)))
                    continue
                m = re.match(r'include\("([^"]+)"\)', stmt)
                if m:
                    if not suppress:
                        expand(m.group(1))
                    continue
                m = re.match(r'(\w+)\s*=\s*(-?\d+)$', stmt)
                if m:
                    var[m.group(1)] = int(m.group(2))
        m = re.match(r'\s*import\s+(\S+)', l)
        if m and not suppress:
            expand(m.group(1))
            continue
        if not suppress:
            out.append((path, i + 1, l))

expand(sys.argv[1])

# strip comments and strings (multi-line /* */)
code = []
inc = False
for f, n, l in out:
    t = l
    r = ''
    j = 0
    while j < len(t):
        if inc:
            k = t.find('*/', j)
            if k < 0:
                j = len(t)
            else:
                inc = False; j = k + 2
            continue
        if t.startswith('/*', j):
            inc = True; j += 2; continue
        if t.startswith('//', j):
            break
        if t[j] == '"':
            k = t.find('"', j + 1)
            j = len(t) if k < 0 else k + 1
            r += '""'
            continue
        if t[j] == "'":
            k = t.find("'", j + 1)
            j = len(t) if k < 0 else k + 1
            r += "0"
            continue
        r += t[j]; j += 1
    code.append((f, n, r))

defs = {}
for idx, (f, n, t) in enumerate(code):
    for m in re.finditer(r'\bfunction\s+([A-Za-z_][\w.]*)\s*\(', t):
        defs.setdefault(m.group(1).lower(), idx)

only = None
if '--only' in sys.argv:
    only = sys.argv[sys.argv.index('--only') + 1].split(',')
seen = set()
for idx, (f, n, t) in enumerate(code):
    if only and not any(o in f for o in only):
        continue
    for m in re.finditer(r'(?<![\w.$#])([A-Za-z_][\w.]*)\s*\(', t):
        name = m.group(1).lower()
        if name in ('function', 'local', 'instance', 'global', 'globals', 'loop', 'while'):
            continue
        d = defs.get(name)
        if d is not None and d > idx:
            key = (name, f)
            if key in seen:
                continue
            seen.add(key)
            df = code[d]
            print('%s:%d  %s()  used before its definition at %s:%d' % (f, n, m.group(1), df[0], df[1]))
print('expanded lines:', len(code))
