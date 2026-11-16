"""Small helpers to analyse EEL2 / JSFX sources (comments/strings blanking, include chain, paren matching)."""
import re, os
inc_re = re.compile(r'(?:<\?\s*include\("([^"]+)"\)|^import\s+(\S+))', re.M)
def chain(f, seen):
    if f in seen or not os.path.exists(f): return
    seen.append(f)
    for m in inc_re.finditer(open(f, encoding='utf-8', errors='replace').read()):
        chain(m.group(1) or m.group(2), seen)
def blank(t):
    """same length: comments, strings, char consts -> spaces (newlines kept)"""
    out = list(t); i = 0; n = len(t)
    def sp(a, b):
        for k in range(a, b):
            if out[k] not in '\r\n': out[k] = ' '
    while i < n:
        if t.startswith('//', i):
            j = t.find('\n', i); j = n if j < 0 else j; sp(i, j); i = j
        elif t.startswith('/*', i):
            j = t.find('*/', i + 2); j = n if j < 0 else j + 2; sp(i, j); i = j
        elif t[i] == '"':
            j = i + 1
            while j < n and t[j] != '"': j += 2 if t[j] == '\\' else 1
            sp(i, j + 1); i = j + 1
        elif t[i] == "'":
            j = t.find("'", i + 1)
            if 0 < j - i <= 6: sp(i, j + 1); i = j + 1
            else: i += 1
        else: i += 1
    return ''.join(out)
def mp(s, i):
    d = 0
    for j in range(i, len(s)):
        if s[j] == '(': d += 1
        elif s[j] == ')':
            d -= 1
            if d == 0: return j
    return -1
