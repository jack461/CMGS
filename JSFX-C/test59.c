
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
 
int main(int argc, char * argv[])
{
   double s=0.0;
   double iii = 0;
   int i, j, k;
   for (i=0; i<1000; i++) 
   {
      for (j=0; j< 1000; j++)
      {
         for (k=0; k < 1000; k++)
         {
            iii += 1; 
            s += 1.0/iii;
         }
      }
   }
   printf("iii = %f   s = %f\n", iii, s);

   exit(0);
}

