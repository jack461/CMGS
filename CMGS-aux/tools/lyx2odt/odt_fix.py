"""Post-process the ODT produced by make4ht from the Game Master manual.

  python3 odt_fix.py in.odt out.odt doc.tex

doc.tex is the file given to make4ht (to find the LaTeX source of each formula).
"""
import re, struct, sys, zipfile, collections
from xml.sax.saxutils import escape

src, dst, texfile = sys.argv[1], sys.argv[2], sys.argv[3]
zin = zipfile.ZipFile(src)
files = {n: zin.read(n) for n in zin.namelist()}
order = zin.namelist()
report = collections.OrderedDict()

IMG_WIDTH_MARGIN = 8.0   # pt left free on the line (4 pt on each side)
KEEP_SIZE = {'ishot-001.png', 'ishot-002.png'}   # the two small "Reload" buttons (figures 2.2, 2.3)

styles = files['styles.xml'].decode('utf-8')
content = files['content.xml'].decode('utf-8')
page_w = float(re.search(r'fo:page-width="([\d.]+)pt"', styles).group(1))
PAGE_TEXT_WIDTH = page_w - 2 * 72.0  # margins of 1 inch


def png_size(data):
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', data[16:24])
    return None


BMK = r"<text:bookmark [^>]*>(?:</text:bookmark>)?"
CMT = r"<!--(?:(?!-->).)*-->"

# ---------------------------------------------------------------- images
# Image frames outside any paragraph (directly in a figure section) are dropped by LibreOffice
out, pos, n = [], 0, 0
for m in re.finditer(r"<draw:frame[^>]*>\s*<draw:image.*?</draw:frame>", content, re.S):
    before = content[:m.start()]
    if before.rfind('<text:p') < before.rfind('</text:p>'):
        out += [content[pos:m.start()], "<text:p text:style-name='Text-body'>" + m.group(0) + "</text:p>"]
        pos = m.end()
        n += 1
out.append(content[pos:])
content = ''.join(out)
report['images wrapped in a paragraph'] = n


# Size : full line width (proportions kept), except the small ones; height from the pixel size
def fix_frame(m):
    frame = m.group(0)
    name = re.search(r"draw:name='([^']+)'", frame).group(1)
    href = re.search(r"xlink:href='([^']+)'", frame).group(1)
    w = float(re.search(r"svg:width='([\d.]+)pt'", frame).group(1))
    size = png_size(files.get(href, b''))
    if not size:
        return frame
    if name not in KEEP_SIZE:
        w = PAGE_TEXT_WIDTH - IMG_WIDTH_MARGIN
    h = w * size[1] / size[0]
    report['images resized'] = report.get('images resized', 0) + 1
    frame = re.sub(r"svg:width='[\d.]+pt'", "svg:width='%.3fpt'" % w, frame)
    return re.sub(r"svg:height='[\d.]+pt'", "svg:height='%.3fpt'" % h, frame)


content = re.sub(r"<draw:frame[^>]*>\s*<draw:image[^>]*>", fix_frame, content)

# Centered : a paragraph holding only an image gets the "GM-Figure" style
FILLER = r"(?:\s|" + CMT + "|" + BMK + ")*"
content, n = re.subn(r"<text:p text:style-name='[^']*'>(" + FILLER + r"<draw:frame[^>]*>\s*<draw:image(?:(?!</text:p>).)*?</draw:frame>" + FILLER + r")</text:p>",
                     r"<text:p text:style-name='GM-Figure'>\1</text:p>", content, flags=re.S)
report['images centered'] = n

# ---------------------------------------------------------------- text
# Description list terms are headings without level (= level 1 for LibreOffice) : ordinary paragraphs
content, n = re.subn(r"<text:h text:style-name='dt'>(.*?)</text:h>", r"<text:p text:style-name='dt'>\1</text:p>", content, flags=re.S)
report['description terms'] = n
# Empty terms (code blocks are lists starting with an empty term) : the extra line before the code
content, n = re.subn(r"<text:p text:style-name='dt'>\s*</text:p>", '', content)
report['empty terms removed'] = n
# ... and an empty paragraph just before such a list : also an extra line
content, n = re.subn(r"<text:p text:style-name='[^']*'>\s*</text:p>(\s*<text:list text:name='list' text:style-name='list'>)", r"\1", content)
report['empty lines before code'] = n
# Citations : TeX4ht writes "[6]" then an empty reference field ("Error: Reference source not found")
content, n = re.subn(r"<text:reference-ref text:ref-name=''[^>]*>.*?</text:reference-ref>", '', content, flags=re.S)
report['empty references removed'] = n
# "<" and ">" were output as "¡" and "¿" (no such character in the source)
n = content.count('¡') + content.count('¿')
content = content.replace('¡', '&lt;').replace('¿', '&gt;')
report['< > restored'] = n

# ---------------------------------------------------------------- page breaks
# Consecutive page breaks separated only by empty paragraphs and comments : a single one,
# "clearpage" (break before, chapter page style : odd page, no header), keeping the bookmarks
BRK = r"<text:p text:style-name='(?:newpage|clearpage)'></text:p>"
FILL = r"(?:\s|" + CMT + r"|<text:p text:style-name='[^']*'>(?:\s|" + BMK + r")*</text:p>)"


def one_break(m):
    return "<text:p text:style-name='clearpage'>" + ''.join(re.findall(BMK, m.group(0))) + "</text:p>"


content, n = re.subn(BRK + "(?:" + FILL + "*" + BRK + ")+", one_break, content, flags=re.S)
report['page break groups'] = n
# no page break at the very end (empty last page)
content = re.sub(BRK + "(" + FILL + "*</office:text>)", lambda m: m.group(1), content, flags=re.S)
# table of contents on its own pages (header "Table des matières")
# (a break paragraph just before the table, if any, is replaced; its bookmarks are kept)
BRKP = r"<text:p text:style-name='(?:newpage|clearpage)'>(?:" + BMK + r")*</text:p>"
i = content.find('<text:table-of-content ')
assert i > 0, 'table of contents not found'
w0 = max(0, i - 4000)  # search only in the text just before the table (fast)
m = re.search(r"(?:" + BRKP + r")?(?:" + FILL + r")*\Z", content[w0:i], re.S)
a = w0 + m.start()
content = (content[:a] + "<text:p text:style-name='GM-Break-TOC'>" + ''.join(re.findall(BMK, m.group(0)))
           + "</text:p>" + content[i:])
# pages 1 and 2 (title, release informations) : no header, no footer
content = content.replace('<office:text>', "<office:text><text:p text:style-name='GM-Start'></text:p>", 1)

# ---------------------------------------------------------------- formulas
# LibreOffice Math misreads TeX4ht's MathML (<mspace>, "And"/"Or" taken as operators, "&" as ∧).
# Each formula gets its StarMath text, which LibreOffice uses.
STARMATH = {
    r'FLM_{dest}\,=\,(FLM_{source}\,\&\,And)\,|\,Or':
        'italic{FLM}_{italic{dest}} ` = ` (italic{FLM}_{italic{source}} ` "&" ` italic{"And"}) ` "|" ` italic{"Or"}',
    r'\frac{N\times(N+1)}{2}': '{N times (N+1)} over 2',
    r'N=10': 'N=10', r'N-1': 'N-1', r'N-2': 'N-2', r'N': 'N',
    r'e': 'e', r'f': 'f', r'E': 'E', r'a': 'a', r'b': 'b', r'x': 'x', r'bx': 'bx',
    r'\forall x\in E,\,f(x,e)=f(e,x)=x': 'forall x in E, ` f(x,e)=f(e,x)=x',
    r'-\infty': '-infinity',
    r'-1.7976931348623158E+308': '"-1.7976931348623158E+308"',
    r'1.7976931348623158E+308': '"1.7976931348623158E+308"',
    r'ax^{2}+bc+c': 'ax^2+bc+c', r'x^{2}': 'x^2', r'ax^{2}': 'ax^2',
    r'a\times x^{2}': 'a times x^2', r'b\times x': 'b times x',
    r'r1=\frac{-b+\sqrt{b^{2}-4ac}}{2a}': 'r1 = {-b + sqrt{b^2 - 4ac}} over {2a}',
    r'O(N^{2})': 'O(N^2)', r'N^{2}': 'N^2', r'2\times2': '2 times 2', r'3\times3': '3 times 3',
}
tex = open(texfile, encoding='utf-8').read()
by_line = collections.defaultdict(list)
for m in re.finditer(r'(?<!\\)\$([^$]{1,200})\$', tex):
    by_line[tex.count('\n', 0, m.start()) + 1].append(m.group(1))
objs = collections.defaultdict(list)
for name in files:
    m = re.match(r'doc-m(\d+)/content\.xml$', name)
    if m:
        line = int(re.search(r'from doc\.tex line (\d+)', files[name].decode('utf-8')).group(1))
        objs[line].append((int(m.group(1)), name))
nmath = missing = 0
for line, lst in objs.items():
    for k, (num, name) in enumerate(sorted(lst)):
        latex = by_line[line][k] if k < len(by_line[line]) else None
        sm = STARMATH.get(latex)
        s = files[name].decode('utf-8')
        s = re.sub(r'<mspace[^>]*>\s*</mspace>|<mspace[^>]*/>', '', s)
        if sm is None:
            missing += 1
            print('no StarMath for line', line, repr(latex))
            s = re.sub(r'(<math[^>]*>)(.*)(</math>)', lambda m: m.group(1) + '<mrow>' + m.group(2) + '</mrow>' + m.group(3), s, flags=re.S)
        else:
            s = re.sub(r'(<math[^>]*>)(.*)(</math>)', lambda m: m.group(1) + '<semantics><mrow>' + m.group(2) + '</mrow>'
                       + '<annotation encoding="StarMath 5.0">' + escape(sm) + '</annotation></semantics>' + m.group(3), s, flags=re.S)
            nmath += 1
        files[name] = s.encode('utf-8')
report['formulas'] = nmath
report['formulas without StarMath'] = missing

# ---------------------------------------------------------------- page styles
new_styles = (
    '<style:style style:name="GM-Header" style:family="paragraph">'
    '<style:paragraph-properties fo:border-bottom="0.5pt solid #000000" fo:padding-bottom="2pt">'
    '<style:tab-stops><style:tab-stop style:position="%.1fpt" style:type="right"/></style:tab-stops>'
    '</style:paragraph-properties>'
    '<style:text-properties fo:font-size="9pt" fo:font-style="italic"/></style:style>'
    '<style:style style:name="GM-Footer" style:family="paragraph">'
    '<style:paragraph-properties fo:text-align="center"/>'
    '<style:text-properties fo:font-size="10pt"/></style:style>'
    '<style:style style:name="GM-Figure" style:family="paragraph">'
    '<style:paragraph-properties fo:text-align="center" fo:text-indent="0pt" fo:margin-left="0pt" fo:margin-right="0pt"'
    ' fo:margin-top="0.2cm" fo:margin-bottom="0.1cm" fo:keep-with-next="always"/></style:style>'
    '<style:style style:name="GM-Start" style:family="paragraph" style:master-page-name="GM-Empty">'
    '<style:text-properties fo:font-size="2pt"/></style:style>'
    '<style:style style:name="GM-Break-TOC" style:family="paragraph" style:master-page-name="GM-TOC"/>'
    % PAGE_TEXT_WIDTH)
styles = styles.replace('</office:styles>', new_styles + '</office:styles>', 1)
styles, n = re.subn(
    r'(<style:page-layout-properties [^>]*?)\s*>\s*</style:page-layout-properties>',
    r'\1 fo:margin-top="1.2cm" fo:margin-bottom="1.0cm"></style:page-layout-properties>'
    '<style:header-style><style:header-footer-properties fo:min-height="0.6cm" fo:margin-bottom="0.5cm"/></style:header-style>'
    '<style:footer-style><style:header-footer-properties fo:min-height="0.6cm" fo:margin-top="0.4cm"/></style:footer-style>',
    styles, count=1)
assert n == 1, 'page layout not found'
# same layout, but always on a right (odd) page : parts and chapters
layout = re.search(r'<style:page-layout style:name="Standard-page-layout">.*?</style:page-layout>', styles, re.S).group(0)
right = layout.replace('style:name="Standard-page-layout"', 'style:name="GM-Right-layout" style:page-usage="right"')
styles = styles.replace(layout, layout + right, 1)

FOOTER = ('<style:footer><text:p text:style-name="GM-Footer">'
          '<text:page-number text:select-page="current"/></text:p></style:footer>')
masters = (
    '<style:master-page style:name="Standard" style:page-layout-name="Standard-page-layout">'
    '<style:header><text:p text:style-name="GM-Header">'
    '<text:chapter text:display="name" text:outline-level="1"/><text:tab/>'
    '<text:chapter text:display="name" text:outline-level="2"/></text:p></style:header>' + FOOTER +
    '</style:master-page>'
    # first page of a part or a chapter : odd page, no header
    '<style:master-page style:name="GM-Chapter" style:page-layout-name="GM-Right-layout" style:next-style-name="Standard">'
    + FOOTER + '</style:master-page>'
    # title and release pages
    '<style:master-page style:name="GM-Empty" style:page-layout-name="Standard-page-layout" style:next-style-name="GM-Empty"/>'
    # table of contents
    '<style:master-page style:name="GM-TOC" style:page-layout-name="Standard-page-layout" style:next-style-name="GM-TOC">'
    '<style:header><text:p text:style-name="GM-Header">Table des matières</text:p></style:header>' + FOOTER +
    '</style:master-page>')
styles, n = re.subn(r'<style:master-page style:name="Standard" style:page-layout-name="Standard-page-layout"\s*/>', masters, styles)
assert n == 1, 'master page not found'
# make4ht gives some paragraph styles an empty page style and a page number 0 : pages after them
# had an empty header and a page number 0
styles = styles.replace(' style:master-page-name=""', '').replace(' style:page-number="0"', '')
styles, n = re.subn(r'(<style:style style:name="clearpage" style:family="paragraph")', r'\1 style:master-page-name="GM-Chapter"', styles)
assert n == 1, 'clearpage style not found'

# the "list" lists (code blocks, labelings) have a space as bullet : with the empty term removed,
# it shifted the first line of code. A zero width space instead.
lst = re.search(r'<text:list-style style:name="list" >.*?</text:list-style>', styles, re.S).group(0)
styles = styles.replace(lst, lst.replace('text:bullet-char=" "', 'text:bullet-char="\u200b"'), 1)
files['styles.xml'] = styles.encode('utf-8')
files['content.xml'] = content.encode('utf-8')

# ---------------------------------------------------------------- write (mimetype first, uncompressed)
with zipfile.ZipFile(dst, 'w') as zout:
    zout.writestr(zipfile.ZipInfo('mimetype'), files['mimetype'], compress_type=zipfile.ZIP_STORED)
    for name in order:
        if name != 'mimetype':
            zout.writestr(name, files[name], compress_type=zipfile.ZIP_DEFLATED)
for k, v in report.items():
    print('%-28s %s' % (k, v))
