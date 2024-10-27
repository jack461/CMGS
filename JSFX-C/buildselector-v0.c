/*
   Build a "n" level selector for JSFX

*/
#include <getopt.h>
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>

#define sz 120
char spaces[121] = "                              "
                   "                              "
                   "                              "
                   "                              " ;
int gl_counter;

void dolevel(int level, char * src, char * dst, int indent, int incrdec)
{
    int val = 1 << level;
    printf("%s(%s & 0x%x) ? (\n", spaces + sz - indent, src, val);
    if (level <= 0) {
        --gl_counter;
        printf("%s///%d///\n", spaces + sz - indent - 4, gl_counter);
        printf("%s%s=%d;\n", spaces + sz - indent - 4, dst, gl_counter);
    } else {
        dolevel(level - 1, src, dst, indent + incrdec, incrdec);
    }
    printf("%s) : (\n", spaces + sz - indent);
    if (level < 1) {
        --gl_counter;
        printf("%s///%d///\n", spaces + sz - indent - 4, gl_counter);
        printf("%s%s=%d;\n", spaces + sz - indent - 4, dst, gl_counter);
    } else {
        dolevel(level - 1, src, dst, indent + incrdec, incrdec);
    }
    printf("%s);\n", spaces + sz - indent);
}

void makeselector(int level, char * src, char * dst, int initdec, int incrdec)
{
    level = (level < 1) ? 1 : (level > 12) ? 12 : level;
    gl_counter = 1 << level; 
    dolevel(level-1, src, dst, initdec, incrdec);
}

int main(int argc, char * argv[])
{
    // makeselector(10, "op", "op_code", 4, 4);
    makeselector(9, "mSL_op", "mSL_Xerr", 8, 0);
    exit(0);
}


