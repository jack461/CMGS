/*
   Build a "n" level selector for JSFX

*/
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include <getopt.h>

#define sz 120
char spaces[sz+1] = "                              "
                   "                              "
                   "                              "
                   "                              " ;
int gl_counter;

char Src[64];
char Err[64];
int indent;
int codsiz;

void printlevel(char * dst, int indent)
{
    char * spc = spaces + sz - indent -4;
    --gl_counter;
    printf("\n");
    printf("%s//++++%d++++//\n", spc, gl_counter);
    printf("%s%s=%d;\n", spc, dst, gl_counter);
    printf("%s//++++%d++++//\n", spc, gl_counter);
    printf("%s", spc + 4);
}

void dolevel(int level, char * src, char * dst, int indent)
{
    int val = 1 << level;
    printf("(%s&0x%x)?(", src, val);
    if (level <= 0) {
        printlevel(dst, indent);
    } else {
        dolevel(level - 1, src, dst, indent);
    }
    printf("):(");
    if (level < 1) {
        printlevel(dst, indent);
    } else {
        dolevel(level - 1, src, dst, indent);
    }
    printf(");");
}

void makeselector(int level, char * src, char * dst, int initdec)
{
    level = (level < 1) ? 1 : (level > 12) ? 12 : level;
    gl_counter = 1 << level; 
    printf("\n%s", spaces + sz - initdec);
    dolevel(level-1, src, dst, initdec);
    printf("\n\n");
}

int main(int argc, char * argv[])
{
    // Provide some default value
    strcpy(Src, "Cmd");
    strcpy(Err, "Err");
    codsiz = 3;
    indent = 4;
    // makeselector(10, "op", "op_code", 4);
    /*
	makeselector(9, "mSL_op", "mSL_errX", 8); // 8 is for 256 different code ops
    */

	makeselector(codsiz, Src, Err, indent);
    exit(0);
}


