

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
 
union {
    double dbl;
    unsigned long int uli;
} uni;


union {
    double dbl;
    struct {
        short i1, i2, i3, i4;
    } i;
} stru, rval;

double dran, dval, dtop, dmax, dmin, dfac, dres, diff, vmax;
long int cnt;
long int lint, lint2;
int int1, int2;
float flt1, flt2;

int main(int argc, char * argv[])
{

    printf("siz-dbl:%lu  siz-short:%lu  siz-stru:%lu  siz-int:%lu  siz-lint:%lu\n",
        sizeof(double), sizeof(short), sizeof(stru), sizeof(int), sizeof(lint));

    lint = 0xFFFFFFFFFFFFL;
    printf("lint=    %ld    %lx\n", lint, lint);

    dran = 1e30,
    dval = 1/dran;
    dtop = dran;
    dfac = 1.00001307;
    dmax = 0;
    dmin = 1e80;
    cnt = 0;


    for (lint=1; lint<0xFFFFFFFFFFFFL; lint+= 0x1001)
    {   
        int1 = (int)((lint >> 24) & 0xFFFFFFL);
        int2 = (int)(lint & 0xFFFFFFL);
        flt1 = (float) int1;
        flt2 = (float) int2;
        int1 = (int) flt1;
        int2 = (int) flt2;
        lint2 = ((long int)int1 << 24) +  (long int)int2;
        dval = (double) lint;
        dres = (double) lint2;
        diff = fabs(dval - dres) / dval;
        if (diff > dmax) { dmax = diff; vmax = dval; }
        if (diff < dmin) dmin = diff;
        cnt += 1;
    }

    printf("cnt:%ld  min:%e   max:%e for %e\n", cnt, dmin, dmax, vmax);
    exit(0);
}


