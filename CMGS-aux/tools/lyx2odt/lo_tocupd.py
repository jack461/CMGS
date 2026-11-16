import uno
from com.sun.star.beans import PropertyValue

def update(*args):
    desktop = XSCRIPTCONTEXT.getDesktop()
    p = PropertyValue(); p.Name = "Hidden"; p.Value = True
    doc = desktop.loadComponentFromURL("file:///PATH/TO/document.odt", "_blank", 0, (p,))
    idx = doc.getDocumentIndexes()
    for k in range(2):   # twice : the table length changes the page numbers
        for i in range(idx.getCount()):
            x = idx.getByIndex(i)
            # never a bibliography made by TeX4ht : LibreOffice would empty it
            if "com.sun.star.text.Bibliography" not in x.getSupportedServiceNames():
                x.update()
    doc.store()
    doc.close(True)
    with open("/tmp/tocupd.done", "w") as f:
        f.write("indexes: %d\n" % idx.getCount())
