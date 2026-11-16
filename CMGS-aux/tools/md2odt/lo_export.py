LOG = "/PATH/TO/workdir/export.log"

def log(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

def doexport(*args):
    import traceback, uno
    from com.sun.star.beans import PropertyValue
    def pv(n, v):
        p = PropertyValue(); p.Name = n; p.Value = v; return p
    try:
        desktop = XSCRIPTCONTEXT.getDesktop()
        doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl("/PATH/TO/workdir/laid.odt"), "_blank", 0, (pv("Hidden", True),))
        idx = doc.getDocumentIndexes()
        for k in range(2):
            for i in range(idx.getCount()):
                x = idx.getByIndex(i)
                if "com.sun.star.text.Bibliography" not in x.getSupportedServiceNames():
                    x.update()
        doc.storeToURL(uno.systemPathToFileUrl("/PATH/TO/Documents/MCBM-Manuel.fodt"), (pv("FilterName", "OpenDocument Text Flat XML"),))
        doc.storeToURL(uno.systemPathToFileUrl("/PATH/TO/Documents/MCBM-Manuel.pdf"), (pv("FilterName", "writer_pdf_Export"),))
        doc.close(True)
        log("OK")
    except Exception:
        log("ERROR " + traceback.format_exc())
