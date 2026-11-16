"""Remap VS Code Bookmarks (bookmarks.json, 0-based lines) of one file after an edit, by text alignment (difflib)."""
import json, difflib
def remap(bmfile, path, oldlines, newlines):
    sm = difflib.SequenceMatcher(None, oldlines, newlines, autojunk=False)
    m = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1): m[i1 + k] = j1 + k
    d = json.load(open(bmfile)); n = 0
    for f in d['files']:
        if f['path'] != path: continue
        for b in f['bookmarks']:
            o = b['line']
            if o in m: b['line'] = m[o]
            else:
                k = o
                while k not in m and k < len(oldlines): k += 1
                b['line'] = m.get(k, len(newlines) - 1)
            n += (b['line'] != o)
    json.dump(d, open(bmfile, 'w'), indent='\t')
    return n
