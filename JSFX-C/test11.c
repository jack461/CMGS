

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
 

union {
    double dbl;
    struct {
        short i1, i2, i3, i4;
    } i;
} stru, rval;

double dran, dval, dtop, dmax, dmin, dfac, dres, diff, vmax;
int cnt;

int main(int argc, char * argv[])
{

    printf("siz-dbl:%lu  siz-short:%lu  siz-stru:%lu\n", sizeof(double), sizeof(short), sizeof(stru));

    dran = 1e20,
    dval = 1/dran;
    dtop = dran;
    dfac = 1.00001307;
    dmax = 0;
    dmin = 1e80;
    cnt = 0;


    while (dval <= dtop)
    {
        stru.dbl = dval;
        rval.i.i1 = stru.i.i1 ;
        rval.i.i2 = stru.i.i2 ;
        rval.i.i3 = stru.i.i3 ;
        rval.i.i4 = stru.i.i4 ;
        dres = rval.dbl;

        diff = fabs(dval - dres) / dval;
        if (diff > dmax) { dmax = diff; vmax = dval; }
        if (diff < dmin) dmin = diff;
        dval = dval * dfac;
        cnt += 1;
    }

    printf("cnt:%d  min:%e   max:%e for %e\n", cnt, dmin, dmax, vmax);
    exit(0);
}


