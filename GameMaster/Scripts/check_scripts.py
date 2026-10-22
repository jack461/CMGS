"""Check the execution of the mSL test scripts against a system log exported by 'p'.

  python3 check_scripts.py [log | project directory] [-s scripts directory] [-a]

The log is a "syslog-<Plugin>-<date>.txt" file. Given a directory, the most recent syslog-*.txt
in it is used; with no argument, the most recent one in ~/Music/REAPER-Projects/*/.

Each script line  // Expected "text"  (or  // Expect "text") announces a line of the output which
must contain "text" ; the text may not end inside a word or a number ("s vaut 55" does not
accept "s vaut 557", nor "s vaut 55.2").
In "text", sprintf formats stand for values which may change from one run to another, e.g.
"Ex-0004. fib = %d" :
  %d %i   an integer                       %x %X   a hexadecimal number
  %f      a number, with or without decimals   %.2f  a number with exactly 2 decimals
  %e %g   a number, exponent allowed       %s      any text (possibly empty)
  %c      one character                    %%      the character % itself
Flags (- + 0 space) and width are accepted : as in sprintf, the width is a minimum field size,
so it allows padding spaces (before the value, or after it with -), not a number of digits.
The output of a script is the part of the log which follows its (last) line
  ::-> Using ".../Ex-0001.mSL"
up to the end of the log : several scripts may be loaded before being run, so their outputs
follow all their "Using" lines. The expected texts must appear in this part, in the order of
the script ; they should therefore name the script (e.g. "Ex-0001. s vaut 55").

A line  // Expected error 1629  announces an error : a log line "ERR: 1629 ..." (compilation)
or "*** ERR: thread: ... Error:1629 ..." (execution, the thread stops) after the "Using" line of
the script. Repeat it to expect the same error several times.
The error lines after the first "Using" which are not expected by a script are reported at the
end, and make the check fail.

FilePlayer writes "*  Compile: .../Ex-0001.mSL" instead of the "Using" line ; the GamePlayer
writes both. Some plug-ins (ScriptMaster) write none of them : a script is then considered as
run from the first log line which begins with its name (e.g. "Ex-0005."), and its output is
the rest of the log. A script which did not compile starts at its "ERR: NNNN can't compile" line.

The first digit of the number of a script tells the plug-ins it runs in : Ex-0NNN (generic
tests of the language) in all of them, Ex-1NNN in Interstys, Ex-2NNN in the GamePlayer, Ex-3NNN in
Diffusion-3. When the plug-in is known from the name of the log, the specific scripts of the other
plug-ins are ignored, and one run in this log is reported as a failure (not checked).

A script run several times : its expected texts are checked in its last run, its expected errors are
expected at each run.

-a : also list the scripts with expectations which were not run in this log.
Exit status : 0 if all the run scripts are correct, 1 otherwise.
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = HERE  # the test scripts are next to this file
PROJECTS = os.path.expanduser('~/Music/REAPER-Projects')
USING = re.compile(r'^(?:::-> Using "(.*)"\s*$|\*\s+(?:Compile|Script):\s+(.*?\.(?:mSL|txt))\s)')
SEPARATOR = '_' * 17
EXPECTED = re.compile(r'//\s*Expect(?:ed)?\s*"([^"]*)"')
EXPECTED_ERR = re.compile(r'//\s*Expect(?:ed)?\s+error\s+(\d+)')
# the plug-in specific series of scripts (first digit of the number), named as in "syslog-<Plugin>-<date>.txt"
SERIES = {'1': 'Interstys', '2': 'GamePlayer', '3': 'Diffusion3'}
SERIES_NAME = re.compile(r'^Ex-(\d)\d{3}\.mSL$')
LOG_PLUGIN = re.compile(r'^syslog-(.+?)-\d{4}-')
COMPILE_FAIL = re.compile(r'^ERR:\s*\d+\s+can.t compile "(.*)"')
ERROR_LINE = re.compile(r'^(?:ERR:\s*(\d+)|\*\*\* ERR:.*?Error:\s*(-?\d+))')


FORMAT = re.compile(r'%([-+0 #]*)(\d*)(?:\.(\d+))?([diufFeEgGxXsc%])')


def conversion(m):
    """The regular expression of one sprintf format."""
    flags, width, prec, conv = m.groups()
    if conv == '%':
        return '%'
    if conv in 'diu':
        r = r'[-+ ]?\d+'
    elif conv in 'fF':
        r = r'[-+ ]?\d+' + ((r'\.\d{%s}' % prec if int(prec) else '') if prec else r'(?:\.\d*)?')
    elif conv in 'eEgG':
        r = r'[-+ ]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?'
    elif conv in 'xX':
        r = r'[0-9a-fA-F]+'
    elif conv == 's':
        r = r'.*?'
    else:
        r = r'.'
    if width and conv != 's':
        r = r + ' *' if '-' in flags else ' *' + r
    return r


def pattern(e):
    """The regular expression of an expected text, with its sprintf formats."""
    r, pos = '', 0
    for m in FORMAT.finditer(e):
        r += re.escape(e[pos:m.start()]) + conversion(m)
        pos = m.end()
    # the text may not end inside a word or a number
    return re.compile(r + re.escape(e[pos:]) + r'(?!\w)(?!\.\d)')


def other_plugin(name, plugin):
    """The plug-in of a specific script, if it is not the plug-in of the log (None otherwise)."""
    m = SERIES_NAME.match(name)
    owner = SERIES.get(m.group(1)) if m else None
    return owner if plugin and owner and owner != plugin else None


def newest_log(d):
    logs = glob.glob(os.path.join(d, 'syslog-*.txt'))
    return max(logs, key=os.path.getmtime) if logs else None


def find_log(arg):
    if arg and os.path.isfile(arg):
        return arg
    if arg:
        return newest_log(arg)
    logs = [l for d in glob.glob(os.path.join(PROJECTS, '*')) for l in [newest_log(d)] if l]
    return max(logs, key=os.path.getmtime) if logs else None


def main():
    args = sys.argv[1:]
    show_all = '-a' in args
    scripts = SCRIPTS
    if '-s' in args:
        i = args.index('-s')
        scripts = args[i + 1]
        del args[i:i + 2]
    args = [a for a in args if a != '-a']
    log = find_log(args[0] if args else None)
    if not log:
        sys.exit('No syslog-*.txt found.')
    m = LOG_PLUGIN.match(os.path.basename(log))
    plugin = m.group(1) if m else None
    print('Log :', log)
    lines = open(log, encoding='utf-8', errors='replace').read().splitlines()
    # a full log (a ring) exported from its start : the newest lines come first, up to the separator ;
    # put them back in chronological order
    sep = next((i for i, l in enumerate(lines) if l.strip() == SEPARATOR), None)
    if sep is not None and any(l.strip() for l in lines[sep + 1:]):
        lines = lines[sep + 1:] + lines[:sep + 1]
        print('(full log : lines put back in chronological order ; the oldest lines are lost)')

    # the output of each run script : from its last "Using" line to the end of the log
    # nruns : how many times each script was run ; firsts : the start of its first run
    runs, first, nruns, firsts = {}, None, {}, {}
    for i, l in enumerate(lines):
        m = USING.match(l)
        if m:
            name = os.path.basename(m.group(1) or m.group(2))
            runs[name] = lines[i + 1:]
            nruns[name] = nruns.get(name, 0) + 1
            firsts.setdefault(name, i)
            first = i if first is None else first
    # without "Using" line : a script starts at the first line beginning with its name
    for path in glob.glob(os.path.join(scripts, '*.mSL')):
        name = os.path.basename(path)
        stem = os.path.splitext(name)[0] + '.'
        if name not in runs:
            k = next((i for i, l in enumerate(lines) if l.startswith(stem)), None)
            if k is not None:
                runs[name] = lines[k:]
                nruns[name] = lines.count(lines[k]) # its first line (its title) at each run
                firsts[name] = k
                first = k if first is None else min(first, k)
    # a script which did not compile has no "Using" line : it starts at its "can't compile" line
    for i, l in enumerate(lines):
        m = COMPILE_FAIL.match(l)
        if m and os.path.basename(m.group(1)) not in runs:
            runs[os.path.basename(m.group(1))] = lines[i:]
            nruns[os.path.basename(m.group(1))] = 1
            firsts[os.path.basename(m.group(1))] = i
            first = i if first is None else min(first, i)
    # the error lines : [index, code, used] (all of them, if no script was found)
    errors = []
    first = 0 if first is None else first
    if True:
        for i in range(first, len(lines)):
            m = ERROR_LINE.match(lines[i])
            if m:
                errors.append([i, int(m.group(1) or m.group(2)), False])
    start = {name: len(lines) - len(out) - 1 for name, out in runs.items()}

    nok = nfail = 0
    for path in sorted(glob.glob(os.path.join(scripts, '*.mSL'))):
        name = os.path.basename(path)
        src = open(path, encoding='utf-8', errors='replace').read()
        expected, experr = EXPECTED.findall(src), [int(c) for c in EXPECTED_ERR.findall(src)]
        owner = other_plugin(name, plugin)
        if owner:
            if name in runs:
                nfail += 1
                print('  ÉCHEC  %s : specific to %s, run in %s (not checked)' % (name, owner, plugin))
            continue
        if name not in runs:
            if show_all and (expected or experr):
                print('  ---    %s : not run' % name)
            continue
        out, pos, missing = runs[name], 0, []
        for e in expected:
            r = pattern(e)
            k = next((j for j in range(pos, len(out)) if r.search(out[j])), None)
            if k is None:
                missing.append(e)
            else:
                pos = k + 1
        errmiss = []
        for c in experr:
            e = next((e for e in errors if e[1] == c and not e[2] and e[0] > start[name]), None)
            if e is None:
                errmiss.append(c)
            else:
                e[2] = True
        # the errors of the previous runs (the texts are checked in the last run only)
        for _ in range(nruns.get(name, 1) - 1):
            for c in experr:
                e = next((e for e in errors if e[1] == c and not e[2] and e[0] > firsts[name]), None)
                if e is not None:
                    e[2] = True
        if not expected and not experr:
            print('  ???    %s : no "// Expected" line' % name)
            continue
        if missing or errmiss:
            nfail += 1
            print('  ÉCHEC  %s' % name)
            for e in missing:
                print('           missing (or out of order) : "%s"' % e)
            for c in errmiss:
                print('           missing error : %04d' % c)
        else:
            nok += 1
            print('  OK     %s (%d%s%s)' % (name, len(expected), ', %d error(s)' % len(experr) if experr else '',
                                         ', %d runs' % nruns[name] if nruns.get(name, 1) > 1 else ''))
    for name in sorted(set(runs) - {os.path.basename(p) for p in glob.glob(os.path.join(scripts, '*.mSL'))}):
        print('  ???    %s : run, but not found in %s' % (name, scripts))
    unexp = [e for e in errors if not e[2]]
    for e in unexp:
        print('  ERR    %s' % lines[e[0]])
    print('%d correct, %d failed, %d unexpected error(s)' % (nok, nfail, len(unexp)))
    sys.exit(1 if nfail or unexp else 0)


main()
