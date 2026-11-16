# Flatten the body of a .fodt into numbered-heading text (for the inventory)
import sys, re, html
import xml.etree.ElementTree as ET
NS = {'text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0','office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
      'table':'urn:oasis:names:tc:opendocument:xmlns:table:1.0','draw':'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0'}
T = '{%s}' % NS['text']; TB = '{%s}' % NS['table']; D = '{%s}' % NS['draw']
root = ET.parse(sys.argv[1]).getroot()
body = root.find('office:body/office:text', NS)
cnt = [0]*10
out = []
def txt(e):
    s = []
    def rec(x):
        if x.tag in (D+'frame',): s.append('[IMG]'); 
        elif x.tag == T+'s': s.append(' ' * int(x.get(T+'c', '1')))
        elif x.tag == T+'tab': s.append('\t')
        elif x.tag == T+'line-break': s.append(' / ')
        elif x.tag in (T+'note',): 
            b = x.find('text:note-body', NS); s.append(' [NOTE: ' + (' '.join(txt(p) for p in b) if b is not None else '') + ']'); return_tail(x); return
        else:
            if x.text: s.append(x.text)
            for c in x: rec(c); 
        if x.tail: s.append(x.tail)
    def return_tail(x):
        if x.tail: s.append(x.tail)
    if e.text: s.append(e.text)
    for c in e: rec(c)
    return ''.join(s)
def walk(e, depth=0):
    for c in e:
        if c.tag == T+'h':
            lvl = int(c.get(T+'outline-level', '1'))
            cnt[lvl-1] += 1
            for i in range(lvl, 10): cnt[i] = 0
            num = '.'.join(str(n) for n in cnt[:lvl])
            out.append('\n' + '#'*lvl + ' ' + num + ' ' + txt(c).strip())
        elif c.tag == T+'p':
            t = txt(c).strip()
            if t: out.append(t)
        elif c.tag == TB+'table':
            for row in c.iter(TB+'table-row'):
                cells = [' '.join(txt(p).strip() for p in cell.iter(T+'p')) for cell in row.findall('table:table-cell', NS)]
                out.append('| ' + ' | '.join(cells) + ' |')
        elif c.tag in (T+'table-of-content', T+'alphabetical-index'):
            out.append('[' + c.tag.split('}')[1] + ']')
        else:
            walk(c, depth+1)
walk(body)
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
