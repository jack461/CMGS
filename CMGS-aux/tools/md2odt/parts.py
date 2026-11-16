"""Parts in a manual made by pandoc + layout.py.

  python3 parts.py in.odt out.odt

In the Markdown source, a part title is a paragraph of custom style "part":

    ::: {custom-style="part"}
    Partie I — Présentation
    :::

This script defines the paragraph style "part" (own page, no header, large centered title) and lists these paragraphs
in the table of contents at the level of the chapters (index-source-style "part", as in the Game Master manual).
"""
import re, sys, zipfile

src, dst = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)
infos = z.infolist()
data = {i.filename: z.read(i.filename) for i in infos}
st = data['styles.xml'].decode('utf-8')
ct = data['content.xml'].decode('utf-8')

# the style "part" : a page of its own (master page of the title page : no header nor footer)
st = re.sub(r'<style:style(?=[^>]*style:name="part")[^>]*?(/>|>.*?</style:style>)', '', st, flags=re.S)
part_style = (
    '<style:style style:name="part" style:display-name="part" style:family="paragraph" style:parent-style-name="Heading"'
    ' style:master-page-name="MCBM-Title" style:class="chapter">'
    '<style:paragraph-properties fo:text-align="center" fo:margin-top="8cm" fo:margin-bottom="0cm"/>'
    '<style:text-properties fo:font-size="24pt" fo:font-weight="bold"/></style:style>')
st = st.replace('</office:styles>', part_style + '</office:styles>', 1)

# the table of contents also lists the paragraphs of style "part", at level 1
m = re.search(r'<text:table-of-content-source\b[^>]*>', ct)
assert m, 'no table of contents'
tag = m.group(0)
new_tag = re.sub(r'\s*text:use-index-source-styles="[^"]*"', '', tag)
new_tag = new_tag[:-1] + ' text:use-index-source-styles="true">'
ct = ct.replace(tag, new_tag, 1)
ct = re.sub(r'(<text:table-of-content-source\b.*?)(</text:table-of-content-source>)',
            lambda mm: mm.group(1) + ('<text:index-source-styles text:outline-level="1">'
                                      '<text:index-source-style text:style-name="part"/></text:index-source-styles>'
                                      if '<text:index-source-styles' not in mm.group(1) else '') + mm.group(2),
            ct, count=1, flags=re.S)

data['styles.xml'] = st.encode('utf-8')
data['content.xml'] = ct.encode('utf-8')
import xml.dom.minidom as dm
dm.parseString(data['styles.xml']); dm.parseString(data['content.xml'])
with zipfile.ZipFile(dst, 'w') as out:
    for i in infos:
        out.writestr(i, data[i.filename], compress_type=zipfile.ZIP_STORED if i.filename == 'mimetype' else zipfile.ZIP_DEFLATED)
print('ok')
