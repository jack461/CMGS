#!/bin/sh
rm -f GP_mSL_scripts.txt GP_txt_configs.txt
ls *.mSL */*.mSL > AAAA 2>/dev/null
ls *.txt */*.txt > BBBB 2>/dev/null
ls config*.mSL */config*.mSL >> BBBB 2>/dev/null
echo "WAVES\nOtherClips" >> BBBB
mv AAAA GM_mSL_scripts.txt
mv BBBB GM_txt_configs.txt
