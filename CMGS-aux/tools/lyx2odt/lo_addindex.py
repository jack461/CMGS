LOG = "/tmp/addindex.log"

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")

def addidx(*args):
    import traceback
    try:
        import uno
        from com.sun.star.beans import PropertyValue
        desktop = XSCRIPTCONTEXT.getDesktop()
        p = PropertyValue(); p.Name = "Hidden"; p.Value = True
        doc = desktop.loadComponentFromURL("file:///PATH/TO/document.odt", "_blank", 0, (p,))
        log("loaded")
        text = doc.getText()
        cur = text.createTextCursor()
        cur.gotoEnd(False)
        text.insertControlCharacter(cur, 0, False)          # paragraph break
        cur.ParaStyleName = "Heading-1"
        cur.PageDescName = "GM-Chapter"                      # new odd page
        cur.OutlineLevel = 1
        text.insertString(cur, "Index", False)
        text.insertControlCharacter(cur, 0, False)
        cur.ParaStyleName = "Text-body"
        cur.setPropertyToDefault("PageDescName")
        cur.OutlineLevel = 0
        log("heading inserted")
        idx = doc.createInstance("com.sun.star.text.DocumentIndex")
        log("created %s" % idx)
        idx.Title = ""
        log("done: idx.Title = ")
        idx.UseAlphabeticalSeparators = True
        log("done: idx.UseAlphabeticalSeparators = True")
        idx.UseCombinedEntries = True
        log("done: idx.UseCombinedEntries = True")
        idx.UsePP = False
        log("done: idx.UsePP = False")
        idx.UseDash = False
        log("done: idx.UseDash = False")
        idx.IsCaseSensitive = False
        log("done: idx.IsCaseSensitive = False")
        loc = uno.createUnoStruct("com.sun.star.lang.Locale"); loc.Language = "fr"; loc.Country = "FR"
        idx.Locale = loc
        log("done: idx.Locale = loc")
        cols = doc.createInstance("com.sun.star.text.TextColumns")
        cols.setColumnCount(2)
        log("done: cols.setColumnCount(2)")
        log("done: idx.TextColumns = cols")
        text.insertTextContent(cur, idx, False)
        log("done: text.insertTextContent(cur, idx, False)")
        log("index inserted")
        indexes = doc.getDocumentIndexes()
        for k in range(2):
            for i in range(indexes.getCount()):
                x = indexes.getByIndex(i)
                if "com.sun.star.text.Bibliography" in x.getSupportedServiceNames():
                    continue
                x.update()
        log("indexes: " + ", ".join("%s %s" % (indexes.getByIndex(i).getName(), indexes.getByIndex(i).getSupportedServiceNames()[0]) for i in range(indexes.getCount())))
        doc.store()
        doc.close(True)
        log("OK")
    except Exception:
        log("ERROR " + traceback.format_exc())
