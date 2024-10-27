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
int codsiz;
int indent;
int tabsiz;

void gerror(char * msg)
{
    fprintf(stderr, "*** Error : %s\n", msg);
    exit(1);
}

void printlevel(int dec)
{
    char * spc = spaces + sz - dec -tabsiz;
    --gl_counter;
    printf("\n");
    printf("%s//++++%d++++//\n", spc, gl_counter);
    printf("%s%s=%d;\n", spc, Err, gl_counter);
    printf("%s//++++%d++++//\n", spc, gl_counter);
    printf("%s", spc + tabsiz);
}

void dolevel(int level, int dec)
{
    int val = 1 << level;
    printf("(%s&0x%x)?(", Src, val);
    if (level <= 0) {
        printlevel(dec);
    } else {
        dolevel(level - 1, dec);
    }
    printf("):(");
    if (level < 1) {
        printlevel(dec);
    } else {
        dolevel(level - 1, dec);
    }
    printf(");");
}

void makeselector(int level)
{
    level = (level < 1) ? 1 : (level > 15) ? 15 : level;
    gl_counter = 1 << level; 
    printf("\n%s", spaces + sz - indent);
    dolevel(level-1, indent);
    printf("\n\n");
}

int main(int argc, char * argv[])
{
    int c, w;
    char * pend;
    // Provide some default value
    strcpy(Src, "Cmd");
    strcpy(Err, "Err");
    codsiz = 3;
    indent = 4;
    tabsiz = 4;
    // decode the parameters
    while ((c = getopt(argc, argv, "b:i:t:")) > 0)
    {
        switch(c)
        {
            case 'b':
                w = strtol(optarg, &pend, 0);
                if (((*optarg)==0) || ((*pend)!=0) || (w < 1) || (w > 12))
                    gerror("Invalid -b argument. A number between 1 and 12 is expected.");
                codsiz = w;
                break;

            case 'i':
                w = strtol(optarg, &pend, 0);
                if (((*optarg)==0) || ((*pend)!=0) || (w < 0) || (w > 40))
                    gerror("Invalid -i argument. A number between 0 and 40 is expected.");
                indent = w;
                break;

            case 't':
                w = strtol(optarg, &pend, 0);
                if (((*optarg)==0) || ((*pend)!=0) || (w < 0) || (w > 10))
                    gerror("Invalid -t argument. A number between 0 and 10 is expected.");
                tabsiz = w;
                break;

        }
    }

    makeselector(codsiz);
    exit(0);
}


