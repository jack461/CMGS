
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
 
int main(int argc, char * argv[])
{
   double eps = 0.00001;
   double s=0.0, c=0.0;
   double iii = 0;
   int i, j, k;
   for (i=0; i<1000; i++) 
   {
      for (j=0; j< 1000; j++)
      {
         for (k=0; k < 1000; k++)
         {
            iii += 1; c += eps;
            s += fabs(sin(c));
         }
      }
   }
   printf("iii = %f   s = %f\n", iii, s);

   exit(0);
}

