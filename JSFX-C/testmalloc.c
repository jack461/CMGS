/*
   malloc test
*/

#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include <getopt.h>

#define cnt 1000000000
#define siz 10000000
#define max 100
void * adds[siz];
void * ptr;

int main(int argc, char * argv[])
{
   int i, j, k;

   for (i=0; i<siz; i++)
   {
      adds[i] = (void *) 0;
   }

   for (j=0; j<cnt; j++)
   {
      k = rand()%siz;
      ptr = adds[k];
      if (ptr == (void *) 0)
      {
         adds[k] = (void *) malloc(1 + rand()%max);
      }
      else
      {
         free(ptr); adds[k] = (void *) 0;
      }
   }

   for (i=0; i<siz; i++)
   {
      ptr = adds[i];
      if (ptr != (void *) 0)
      {
         free(ptr); adds[k] = (void *) 0;
      }
   }

   exit(0);
};

