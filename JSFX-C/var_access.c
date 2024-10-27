/*
    Build access to JSFX vars by name
    Jack461 - April 2023
*/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <getopt.h>

char *string;
char ** wordspts;
char ** aliaspts;
char * wordsflgs;
int wcount, wcount_1;
int rocount;

#define sz 120
char spaces[sz+1] =   "                              "
                      "                              "
                      "                              "
                      "                              " ;
char genstr[16];
char Src[64];
char Sep[64];
char xedsep[80];
char msgerr[64];
char inFile[256];
char * spc;
int cmmnt;
int indent;
int tabsiz;

int first, last;
int prvdef;
int pivot;
int count = 1024;
int dbg;

void usage(void)
{
    printf("\n");
    printf("var_access: Provide access to JSFX variables to mSL codes.\n");
}


void gerror(char * msg)
{
    fprintf(stderr, "*** Error : %s\n", msg);
    usage();
    exit(1);
}


void printlevel(int val)
{
    spc = spaces + sz - indent - tabsiz;
    printf("\n");
    sprintf(xedsep, Sep, val);
    if (cmmnt & 1) printf("%s%s\n", spc, xedsep);
    if ((val >= 1) && (val <= wcount))
        if (wordsflgs[val-1] == 0) {
            printf("%s%s%s;\n", spc, aliaspts[val-1],genstr);
        } else {
            printf("%s%s;\n", spc, aliaspts[val-1]);
        }
    else
        printf("%sUndef;\n", spc); 
    if (cmmnt & 2) printf("%s%s\n", spc, xedsep);
    printf("%s", spc + tabsiz);
}


void dolevel(int piv, int fst, int lst)
{
    int lvz = fst >= lst;
    int pv2, pv3;
    if (dbg & 1) {
        printf("\n  cnt: %d    piv:%d  --  fst:%d  --  lst:%d  --  lvz:%d\n", count, piv, fst, lst, lvz);
    }
    if (dbg & 2) {
        count -=1;
    }

  if (count > 0) {

    printf("(%s<%d)?(", Src, piv);
    if (piv <= fst) // if (lvz)
    {
        printlevel(piv-1);
    }
    else
    {
        pv2 = (fst+piv-1)/2;
        dolevel(pv2, fst, piv-1);
    }

    printf("):(");

    if (piv >= lst) // if (lvz)
    {
        printlevel(piv);
    }
    else
    {
        pv3 = (piv+1+lst)/2;
        dolevel(pv3, piv+1, lst);
    }

    printf(");");
  }
}


void makeselector(void)
{
    spc = spaces + sz - indent ;
    printf("\n%s", spc);
    first += 1 - prvdef;
    last += prvdef;
    dolevel(pivot, first, last);
    printf("\n\n");
}


void setparameters(void)
{
    // Provide some default value
    strcpy(Src, "wrd");
    strcpy(Sep, "//=== %i ===//");
    cmmnt = 1;
    indent = 4;
    tabsiz = 4;
    prvdef = 0;
    first = 0;
    last = 7;
    pivot = -1;
}

void readfile(char * fn)
{
    FILE *f = fopen(fn, "rb");
    if (f == NULL) {
         sprintf(msgerr, "Can't open file \"%s\".", fn);
         gerror(msgerr);
    }
    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);  /* same as rewind(f); */

    string = (char *) malloc(fsize + 1);
    if (string == (char*)0) 
        gerror("Can't allocate input string");
    fread(string, fsize, 1, f);
    string[fsize] = 0;
    fclose(f);

}

int countwords(char * pc, int sav)
{
    int siz = 0;
    char c;
    int stat = 0;
    rocount = 0;

    while ((c = *pc) > 0) 
    {
        switch (stat) {
        case 0 :
            if ((c == ' ') || (c == '\n') || (c == '\t') || (c == '\r')) {
                if (sav) {
                    *pc = 0; 
                }
                pc++;
            } else
            if (((c >= 'A') && (c <= 'Z')) || ((c >= 'a') && (c <= 'z')) || (c == '_') || (c == '#')) {
                if (sav) {
                    wordspts[siz] = pc;
                    aliaspts[siz] = pc;
                }
                stat = 1;
                siz += 1;
                pc++;
            } else
            if (c == '-') {
                while ((c != '\n') && (c != '\n') && (c != 0)) 
                {
                    pc++; c = *pc;
                }
            }
            else
            {
               gerror("Unexpected char");
            }
            break;
        case 1 :
            if (((c >= 'A') && (c <= 'Z')) || ((c >= 'a') && (c <= 'z')) || ((c >= '0') && (c <= '9')) || (c == '_')) {
                pc++;
            } else
            if (c == '!') {
               if (sav) {
                   wordsflgs[siz-1] = 1; // flag "read only"
                   rocount += 1;
                   *pc = 0;
               }
               pc ++;
               stat = 0;
            } else
            if (c == '@') {
                if (sav) {
                   wordsflgs[siz-1] = 1; // flag "read only"
                   aliaspts[siz-1] = pc + 1;
                   rocount += 1;
                   *pc = 0;
                }
                stat = 2;
                pc ++;
            }
            else
            {
               stat = 0;
            }
            break;
        case 2 :
            if (c == '@') {
               if (sav) {
                  *pc = 0;
               }
               stat = 0;
            }
            pc ++;
            break;
        }
    }
    return siz;
}

void sortwords(void)
{
    int i, j;
    char * pc;
    int temp;
    for (i=0; i<wcount; i++) 
    {
        for (j=i+1; j<wcount; j++)
        {
            if (strcasecmp((char *)wordspts[i], (char *)wordspts[j]) > 0) {
                pc = wordspts[i]; wordspts[i] = wordspts[j]; wordspts[j] = pc;
                pc = aliaspts[i]; aliaspts[i] = aliaspts[j]; aliaspts[j] = pc;
                temp = wordsflgs[i]; wordsflgs[i] = wordsflgs[j]; wordsflgs[j] = temp;
            }
        }
    }
}

void build_get()
{
    first = 0;
    last = wcount+1;
    pivot = (first + last + 1) / 2;
    strcpy(genstr, "");
    printf("function mSL_vGet(vname)\n");
    printf("local(wrd)\n");
    printf("(\n");
    printf("    wrd = mSL_get_var_idt(vname);\n");
    makeselector();
    printf(");\n"); 
}


void build_set()
{
    first = 0;
    last = wcount+1;
    pivot = (first + last + 1) / 2;
    strcpy(genstr, "=value");
    printf("function mSL_vSet(vname, value)\n");
    printf("local(wrd)\n");
    printf("(\n");
    printf("    wrd = mSL_get_var_idt(vname);\n");
    makeselector();
    printf(");\n"); 
}

int main(int argc, char * argv[])
{
    int l, c;

    strcpy(inFile, "GM_var_names.txt");
    // decode the parameters
    while ((c = getopt(argc, argv, "f:h")) > 0)
    {
        switch(c)
        {
            case '?':
                sprintf(msgerr, "Unknown option: \"%c\".", optopt);
                gerror(msgerr);

            case 'h':
                usage();
                exit(0);

            case 'f':
                strncpy(inFile, optarg, 255);
                break;
        }
    }


    readfile(inFile);
    // printf("String size = %lu\n", strlen(string));
    if (strlen(string) <= 0)
        gerror("Empty input");
    wcount = countwords((char *) string, 0);
    if (wcount <= 0)
        gerror("No identifiers");
    // printf("//   Word count = %d\n", wcount);
    wordspts = malloc(sizeof(char *)*wcount);
    if (wordspts <= 0)
        gerror("Can't allocate name table");
    aliaspts = malloc(sizeof(char *)*wcount);
    if (aliaspts <= 0)
        gerror("Can't allocate alias table");
    wordsflgs = malloc(sizeof(char)*wcount);
    if (wordsflgs <= 0)
        gerror("Can't allocate flags table");
    memset(wordsflgs, 0, wcount);
    wcount_1 = countwords((char *) string, 1);
    if (wcount_1 != wcount)
        gerror("Incorrect analysis");
    wcount_1 --;
    sortwords();

    printf("//  Access to JSFX vars\n\n//    This file is automatically generated\n");
    printf("//    Do not change its contents\n\n@init\n\n\n");
    printf("//   Read-Only vars count = %d\n", rocount);
    /*
    for (l=0; l<wcount; l++) {
        printf("%5d  %s\n", l, wordspts[l]);
    }
    */
    for (l=0; l<wcount_1; l++) {
        if (strcasecmp((char *)wordspts[l], (char *)wordspts[l+1]) == 0) {
             printf("//  Duplicate:  %5d  %s\n", l, wordspts[l]);
        }
    }
    printf("mSL_JSFX_var_count = %d;\n", wcount);
    printf("function mSL_dcl_JSFX_vars()\n");
    printf("(\n");
    printf("    mSL_JSFX_var_count = %d;\n", wcount);
    for (l=0; l<wcount; l++) {
        printf("    mSL_def_JSFX_var(%d, \"%s\");\n", l+1, wordspts[l]);
    }
    printf(");\n"); 

    setparameters();

    build_get();
    build_set();
    exit(0);
}





