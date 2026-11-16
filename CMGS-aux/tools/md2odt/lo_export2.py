CONF = "/PATH/TO/scratch/export2.json"   # {"src": ..., "fodt": ..., "pdf": ... or "", "log": ...}

def doexport2(*args):
    import json, traceback, uno
    from com.sun.star.beans import PropertyValue
    c = json.load(open(CONF))
    def log(m):
        with open(c["log"], "a") as f: f.write(m + "\n")
    def pv(n, v):
        p = PropertyValue(); p.Name = n; p.Value = v; return p
    try:
        desktop = XSCRIPTCONTEXT.getDesktop()
        doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(c["src"]), "_blank", 0, (pv("Hidden", True),))
        idx = doc.getDocumentIndexes()
        for k in range(2):
            for i in range(idx.getCount()):
                x = idx.getByIndex(i)
                if "com.sun.star.text.Bibliography" not in x.getSupportedServiceNames():
                    x.update()
        if c.get("fodt"): doc.storeToURL(uno.systemPathToFileUrl(c["fodt"]), (pv("FilterName", "OpenDocument Text Flat XML"),))
        if c.get("pdf"): doc.storeToURL(uno.systemPathToFileUrl(c["pdf"]), (pv("FilterName", "writer_pdf_Export"),))
        doc.close(True)
        log("OK")
    except Exception:
        log("ERROR " + traceback.format_exc())
