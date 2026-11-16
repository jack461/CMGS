import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
pat = re.compile(r'(?<!\\)\$[^$]{1,200}\$|\\\[.*?\\\]|\\begin\{(equation|align|eqnarray)\*?\}.*?\\end\{\1\*?\}', re.S)
ms = list(pat.finditer(t))
print(len(ms))
for m in ms:
    line = t.count('\n', 0, m.start()) + 1
    print(line, repr(m.group(0)[:110]))
