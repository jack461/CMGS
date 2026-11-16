"""Layout of a pandoc ODT like the Game Master manual.

  python3 layout.py in.odt out.odt

A4, margins 2.54 cm; numbered headings (1, 1.1, 1.1.1); header "chapter | section", footer page number;
title page without header/footer; table of contents on its own pages (header "Table des matières");
each chapter on a new page (no header on its first page); thin borders in tables.
"""
import re, sys, zipfile

src, dst = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)
infos = z.infolist()
data = {i.filename: z.read(i.filename) for i in infos}
st = data['styles.xml'].decode('utf-8')
ct = data['content.xml'].decode('utf-8')
TEXT_W = 21.0 - 2 * 2.54


def sub1(pat, new, s, flags=re.S):
    s2, n = re.subn(pat, new, s, count=1, flags=flags)
    assert n == 1, 'not found: ' + pat[:60]
    return s2


# ---- page layout : A4, header, footer
st = sub1(r'<style:page-layout style:name="Mpm1">.*?</style:page-layout>',
          '<style:page-layout style:name="Mpm1"><style:page-layout-properties fo:page-width="21cm" fo:page-height="29.7cm"'
          ' style:num-format="1" style:print-orientation="portrait" fo:margin-top="1.2cm" fo:margin-bottom="1cm"'
          ' fo:margin-left="2.54cm" fo:margin-right="2.54cm" style:writing-mode="lr-tb"/>'
          '<style:header-style><style:header-footer-properties fo:min-height="0.6cm" fo:margin-bottom="0.5cm"/></style:header-style>'
          '<style:footer-style><style:header-footer-properties fo:min-height="0.6cm" fo:margin-top="0.4cm"/></style:footer-style>'
          '</style:page-layout>', st)

FOOTER = '<style:footer><text:p text:style-name="MCBM-Footer"><text:page-number text:select-page="current"/></text:p></style:footer>'
masters = (
    '<style:master-page style:name="Standard" style:page-layout-name="Mpm1">'
    '<style:header><text:p text:style-name="MCBM-Header">'
    '<text:chapter text:display="number-and-name" text:outline-level="1"/><text:tab/>'
    '<text:chapter text:display="number-and-name" text:outline-level="2"/></text:p></style:header>' + FOOTER +
    '</style:master-page>'
    '<style:master-page style:name="MCBM-Chapter" style:page-layout-name="Mpm1" style:next-style-name="Standard">' + FOOTER +
    '</style:master-page>'
    '<style:master-page style:name="MCBM-Title" style:page-layout-name="Mpm1" style:next-style-name="MCBM-Title"/>'
    '<style:master-page style:name="MCBM-TOC" style:page-layout-name="Mpm1" style:next-style-name="MCBM-TOC">'
    '<style:header><text:p text:style-name="MCBM-Header">Table des matières</text:p></style:header>' + FOOTER +
    '</style:master-page>')
st = sub1(r'<style:master-page style:name="Standard".*?</style:master-page>', masters, st)

# ---- paragraph styles
new_styles = (
    '<style:style style:name="MCBM-Header" style:family="paragraph">'
    '<style:paragraph-properties fo:border-bottom="0.5pt solid #000000" fo:padding-bottom="2pt">'
    '<style:tab-stops><style:tab-stop style:position="%.2fcm" style:type="right"/></style:tab-stops></style:paragraph-properties>'
    '<style:text-properties fo:font-size="9pt" fo:font-style="italic"/></style:style>'
    '<style:style style:name="MCBM-Footer" style:family="paragraph">'
    '<style:paragraph-properties fo:text-align="center"/><style:text-properties fo:font-size="10pt"/></style:style>'
    '<style:style style:name="MCBM-Break-TOC" style:family="paragraph" style:master-page-name="MCBM-TOC"/>'
    % TEXT_W)
st = st.replace('</office:styles>', new_styles + '</office:styles>', 1)
# chapters on a new page (first page without header)
st = sub1(r'<style:style(?=[^>]*style:name="Heading_20_1")', '<style:style style:master-page-name="MCBM-Chapter"', st)
# title page : Title, Subtitle, Author, Date (not defined by pandoc : replaced if present)
for name in ('Title', 'Subtitle', 'Author', 'Date'):
    st = re.sub(r'<style:style(?=[^>]*style:name="%s")[^>]*?(/>|>.*?</style:style>)' % name, '', st, flags=re.S)
title_styles = (
    '<style:style style:name="Title" style:family="paragraph" style:parent-style-name="Heading" style:master-page-name="MCBM-Title">'
    '<style:paragraph-properties fo:text-align="center" fo:margin-top="6cm" fo:margin-bottom="0.6cm"/>'
    '<style:text-properties fo:font-size="26pt" fo:font-weight="bold"/></style:style>'
    '<style:style style:name="Subtitle" style:family="paragraph" style:parent-style-name="Heading">'
    '<style:paragraph-properties fo:text-align="center" fo:margin-bottom="3cm"/>'
    '<style:text-properties fo:font-size="16pt"/></style:style>'
    '<style:style style:name="Author" style:family="paragraph" style:parent-style-name="Standard">'
    '<style:paragraph-properties fo:text-align="center" fo:margin-bottom="0.3cm"/>'
    '<style:text-properties fo:font-size="14pt" fo:font-weight="bold"/></style:style>'
    '<style:style style:name="Date" style:family="paragraph" style:parent-style-name="Standard">'
    '<style:paragraph-properties fo:text-align="center"/>'
    '<style:text-properties fo:font-size="12pt" fo:font-style="italic"/></style:style>')
st = st.replace('</office:styles>', title_styles + '</office:styles>', 1)

# ---- numbered headings : 1, 1.1, 1.1.1
def level(n):
    return ('<text:outline-level-style text:level="%d" style:num-format="1" text:display-levels="%d">'
            '<style:list-level-properties text:list-level-position-and-space-mode="label-alignment">'
            '<style:list-level-label-alignment text:label-followed-by="space"/></style:list-level-properties>'
            '</text:outline-level-style>' % (n, n))
for n in (1, 2, 3):
    st = sub1(r'<text:outline-level-style style:num-format="" text:level="%d">.*?</text:outline-level-style>' % n, level(n), st)

# ---- content : table of contents on its own pages, borders in tables
ct = sub1(r'(<text:table-of-content)', r'<text:p text:style-name="MCBM-Break-TOC"/>\1', ct)
border = 'fo:border="0.5pt solid #808080" fo:padding="0.08cm"'
ct = ct.replace('<style:table-cell-properties fo:border="none" />', '<style:table-cell-properties %s />' % border)

data['styles.xml'] = st.encode('utf-8')
data['content.xml'] = ct.encode('utf-8')
import xml.dom.minidom as dm
dm.parseString(data['styles.xml']); dm.parseString(data['content.xml'])
with zipfile.ZipFile(dst, 'w') as out:
    for i in infos:
        out.writestr(i, data[i.filename], compress_type=zipfile.ZIP_STORED if i.filename == 'mimetype' else zipfile.ZIP_DEFLATED)
print('ok')
