
# mSL Scripts

This directory contains a few "mSL" scripts that may be used to test the mSL byte code compiler/interpreter included in "GameMaster", "Diffusion-3" or "Interstys".

The scripts "Ex-NNNN.mSL" announce their expected output with lines such as
`// Expected "Ex-0001. s vaut 55"` (sprintf formats like `%d` or `%.2f` are allowed) or
`// Expected error 1629`. After running them in a plug-in, export the system log to a file
('p'), then check it with:

    python3 check_scripts.py [log file | project folder] [-a]

(by default, the most recent "syslog-*.txt" of ~/Music/REAPER-Projects/*/).
