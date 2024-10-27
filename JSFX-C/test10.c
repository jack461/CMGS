#include <stdlib.h>
#include <stdio.h>
#include <math.h>
 

double dran, dval, dtop, dmax, dmin, dfac, dres, diff, vmax;
float flt, flt1, flt2;
int cnt;

int main(int argc, char * argv[])
{
   dran = 1e20,
   dval = 1/dran;
   dtop = dran;
   dfac = 1.00001307;
   dmax = 0;
   dmin = 1e80;
   cnt = 0;

   while (dval <= dtop) 
   {
      /*
      flt = (float)dval;
      dres = (double)flt;
      */

      /*
      dres = (double)(float)dval;
      */

      flt = (float)dval;
      flt1 = (float) (dval - (double)flt);
      dres = (double)flt + (double)flt1;
      /*
      */

      /*
      flt = (float)dval;
      flt1 = (float) (dval - (double)flt);
      dres = (double)flt + (double)flt1;
      flt2 = (float) (dval - dres);
      dres = dres + (double)flt2;
      */

      /*
      flt = (float)dval;
      dval = (double)flt;
      flt1 = (float)dval;
      dres = (double)flt1;
      */

      diff = fabs(dval - dres) / dval;
      if (diff > dmax) { dmax = diff; vmax = dval; }
      if (diff < dmin) dmin = diff;
      dval = dval * dfac;
      cnt += 1;
   }

   printf("cnt:%d  min:%e   max:%e for %e\n", cnt, dmin, dmax, vmax);

   exit(0);
}


