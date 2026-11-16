# Paren balance of JSFX/EEL2 sources, skipping // and /* */ comments,
# "strings" and 'char' constants. Also flags an @section opened with
# a pending "(" and extra ")". Usage: python3 -I paren_balance.py file...
import sys
def scan(path):
    s = open(path, encoding='utf-8', errors='replace').read()
    i, n, line = 0, len(s), 1
    depth = 0; stack = []; issues = []
    sec = None; secdepth = {}
    while i < n:
        c = s[i]
        if c == '\n':
            line += 1
            if s.startswith('@', i+1):
                if depth: issues.append((line, 'section start with depth %d' % depth))
            i += 1; continue
        if s.startswith('//', i):
            j = s.find('\n', i); i = n if j < 0 else j; continue
        if s.startswith('/*', i):
            j = s.find('*/', i+2); seg = s[i:(n if j<0 else j+2)]
            line += seg.count('\n'); i = n if j < 0 else j+2; continue
        if c in '"\'':
            j = i+1
            while j < n and s[j] != c:
                if s[j] == '\\': j += 1
                if j < n and s[j] == '\n': line += 1
                j += 1
            i = j+1; continue
        if c == '(':
            depth += 1; stack.append(line)
        elif c == ')':
            if depth == 0: issues.append((line, 'extra )'))
            else: depth -= 1; stack.pop()
        i += 1
    return depth, stack, issues
for p in sys.argv[1:]:
    d, st, iss = scan(p)
    print(p.split('/')[-1], 'balance', d, 'unclosed at', st[:10], 'issues', iss[:10])
