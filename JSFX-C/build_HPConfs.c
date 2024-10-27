/*
    Compute some HP Confs from Their spatial implantation
*/
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include <math.h>
#include <getopt.h>

// Numérotation des HP: 1 à N

// Nombre max. de HP: 0 à 128
#define HPCntMax 129

// Matrices de HP
#define HPMatsz (HPCntMax*HPCntMax)

// Definition des positions de HP
#define HPdefSz (4*HPCntMax + 8)

#define CFdfsSiz 4096
int CFdfs[CFdfsSiz];


float HPdpos[HPdefSz] = {
// <hp num>, "x position", "y position", "z position"
//--- Couche 1
// Elévation de la couche 2
#define h1val 1.30
#define h1valc 2.00
// Elévation de la couche 3
#define h2val 2.75
#define h2valc 2.35
1, 0, 0, 0, 
2, 0, 2, 0,
3, 0, 4, 0,
4, 0, 6, 0,
5, 2, 6, 0,
6, 4, 6, 0,
7, 6, 6, 0,
8, 6, 4, 0,
9, 6, 2, 0,
10, 6, 0, 0,
11, 4, 0, 0,
12, 2, 0, 0,
13, 2, 2, 0,
14, 2, 4, 0,
15, 4, 4, 0,
16, 4, 2, 0,
//--- Couche 2
17, 0, 0, h1val,     
18, 0, 2, h1val,
19, 0, 4, h1val,
20, 0, 6, h1val,
21, 2, 6, h1val,
22, 4, 6, h1val,
23, 6, 6, h1val,
24, 6, 4, h1val,
25, 6, 2, h1val,
26, 6, 0, h1val,
27, 4, 0, h1val,
28, 2, 0, h1val,
29, 2, 2, h1valc,
30, 2, 4, h1valc,
31, 4, 4, h1valc,
32, 4, 2, h1valc,
//--- Couche 3
33, 1, 0, h2valc,
34, 1, 3, h2valc,
35, 1, 6, h2valc,
36, 3, 6, h2val,
37, 5, 6, h2valc,
38, 5, 3, h2valc,
39, 5, 0, h2valc,
40, 3, 0, h2val,
41, 3, 2, h2val,
42, 3, 4, h2val,
-1, -1, -1, -1, -1
};

char msgerr[64];

float HP_x[HPCntMax];
float HP_y[HPCntMax];
float HP_z[HPCntMax];

float wa1[HPCntMax];
int wa2[HPCntMax];
int wa3[HPCntMax];
int wa4[HPCntMax];

float HP_Distances[HPMatsz];

int HP_Proxim[HPMatsz];
int HP_Distant[HPMatsz];

int lastHP;
int lastCF;


void usage(void)
{   
    printf("\n");
    printf("build_HPConfs: construc HP Confs from spatial positions\n");
}

void gerror(char * msg)
{
    fprintf(stderr, "*** Error : %s\n", msg);
    usage();
    exit(1);
}


float dist(float xa, float ya, float za, float xb, float yb, float zb)
{
    return sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb) + (za-zb)*(za-zb));
}


int defC(int num, int siz)
{
    if (num == 0) { num = lastCF; }
    if (CFdfs[num] != 0) {
        while (CFdfs[num] != 0) {
            num = (num + 1) % CFdfsSiz;
        };
        lastCF = num;
    }
    printf("%04d  %02d   ", num, siz);
    if (siz > 32) { printf("\n      "); }
    CFdfs[num] = siz + 3;
    return num;
}


void dfCnf2(int conf, int h1, int h2)
{
    defC(conf, 2);
    printf("%02d %02d    0\n", h1, h2);
}

void dfCnf3(int conf, int h1, int h2, int h3)
{
    defC(conf, 3);
    printf("%02d %02d %02d    0\n", h1, h2, h3);
}


void bdHPpos(void)
{
    int i, j, k, n, d;
    int p, q, y;
    float x;
    lastHP = 0;
    lastCF = 0;
    for(i=0; i<CFdfsSiz; i++) {
        CFdfs[i] = 0;
    }
    CFdfs[0] = -1; // do not use entry 0
    for(i=0; i<HPCntMax; i++) {
        HP_x[i] = HP_y[i] = HP_z[i] = 0;
    }
    k = 0;
    while ((n = HPdpos[k]) >=0) {
         if (n > lastHP) { lastHP = n; };
         HP_x[n] = HPdpos[++k];
         HP_y[n] = HPdpos[++k];
         HP_z[n] = HPdpos[++k];
         ++k;
    }

    for(i=0; i<HPMatsz; i++) {
        HP_Distances[i] = 0;
    }

    for(i=0; i<lastHP; i++) {
        for(j=i+1; j<=lastHP; j++) {
            d = (HP_x[i] - HP_x[j]) * (HP_x[i] - HP_x[j])
              + (HP_y[i] - HP_y[j]) * (HP_y[i] - HP_y[j])
              + (HP_z[i] - HP_z[j]) * (HP_z[i] - HP_z[j]);
            HP_Distances[i+j*HPCntMax] = HP_Distances[j+i*HPCntMax] = sqrt(d);
        }
    }

    for(i=1; i<=lastHP; i++) {
        k = i * HPCntMax + 1;
        for (j=0; j<lastHP; j++) {
            wa1[j] = HP_Distances[k+j];           
            wa2[j] = j+1;
        }
        // Sort wa2 according to wa1
        for (p = 0; p < lastHP-1; p++) {
            for(q = p+1; q < lastHP; q++) {
                if (wa1[p] > wa1[q]) {
                    x = wa1[p]; wa1[p] = wa1[q]; wa1[q] = x;      
                    y = wa2[p]; wa2[p] = wa2[q]; wa2[q] = y;      
                }
            }
        }
        for (j=0; j<lastHP; j++) {
            HP_Proxim[k+j] = wa2[j];
            HP_Distant[k+j] = wa2[lastHP-j-1];
        }
    }
}


// Calculer des lignes
void mklines(int cbase, int fx, int fy, int fz)
{
    int i, j, k, m, n, pt, ln;
    float x, px, py, pz;
    for(j=0; j<HPCntMax; j++) wa4[j] = 1;
    ln = 0;
    for(i=1; i<=lastHP; i++)
    {
        for(j=0; j<HPCntMax; j++) { wa3[j] = 0; wa1[j] = 0; }
        // Lignes including "i"
        wa3[0] = i; pt = 1;
        wa4[i] = 0;
        px = HP_x[i];
        py = HP_y[i];
        pz = HP_z[i];
        for(k=1; k<=lastHP; k++) {
            if (wa4[k] && (fx || px==HP_x[k]) && (fy || py==HP_y[k]) && (fz || pz==HP_z[k]))
            {
                wa3[pt++] = k; wa4[k] = 0;
            }
        }
        if (pt > 1) {
           // there is a line
           ln += 1;
           // Sort according to some criteria
           if (fx == 1) {
               for (k=0; k<pt; k++) wa1[k] = HP_x[wa3[k]];
           }
           if (fy == 1) {
               for (k=0; k<pt; k++) wa1[k] = HP_y[wa3[k]];
           }
           if (fz == 1) {
               for (k=0; k<pt; k++) wa1[k] = HP_z[wa3[k]];
           }
           // sort result
           for (m=0; m<pt-1; m++) {
               for(n=m+1; n<pt; n++) {
                  if (wa1[m] > wa1[n]) {
                      x = wa1[m]; wa1[m] = wa1[n]; wa1[n] = x;
                      k = wa3[m]; wa3[m] = wa3[n]; wa3[n] = k;
                  }
               }
           }
           //printf("%04d  %02d   ", cbase+ln, pt);
           defC(cbase+ln, pt);
           for (k=0; k<pt; k++) {
               printf("%02d ", wa3[k]);
           }
           printf("   0\n");
        }
    }
}

        
void cnfprt(int * tab, int cbase, int l, int cnt)
{
    int i, k;
    defC(cbase+l, cnt);
    /*
    if (cnt > 25) {
        printf("%04d  %02d\n    ", cbase+l, cnt);
    } else {
        printf("%04d  %02d   ", cbase+l, cnt);
    }
    */
    k = l * HPCntMax + 1;
    for (i=0; i< cnt; i++) {
        printf("%02d ", tab[k+i]);
    }
    printf("   0\n");
}


void mkpoints(int * tab, int cbase)
{
    int i;
    for (i=1; i<=lastHP; i++) {
        defC(cbase+i, 1);
        printf("%02d    0\n", tab[i*HPCntMax+1]);
    }
}


void mkpair(int cbase, int pt, float dx, float dy, float dz)
{
    float px, py, pz;
    int i, w;
    px = HP_x[pt] + dx; py = HP_y[pt] + dy; pz = HP_z[pt] + dz;
    w=0; 
    for (i=1; i<=lastHP && w==0; i++) {
        if (HP_x[i] == px && HP_y[i] == py && HP_z[i] == pz) {
            w = i; 
        }
    }
    if (w != 0) {
        dfCnf2(cbase, pt, w);
    }
}


void mkqcu(int cbase, float dst)
{
    int i, j, k, pt, cf;
    cf = 0;
    /*
        printf("// i=%d  j=%d  dist=%f\n", 2, 3, HP_Distances[2*HPCntMax+3]);
        printf("// i=%d  j=%d  dist=%f\n", 2, 17, HP_Distances[2*HPCntMax+17]);
        printf("// i=%d  j=%d  dist=%f\n", 2, 18, HP_Distances[2*HPCntMax+18]);
        printf("// i=%d  j=%d  dist=%f\n", 2, 19, HP_Distances[2*HPCntMax+19]);
        printf("// i=%d  j=%d  dist=%f\n", 2, 30, HP_Distances[2*HPCntMax+30]);
        printf("// i=%d  j=%d  dist=%f\n", 18, 2, HP_Distances[18*HPCntMax+2]);
        printf("// i=%d  j=%d  dist=%f\n", 3, 13, HP_Distances[3*HPCntMax+13]);
        printf("// i=%d  j=%d  dist=%f\n", 5, 31, HP_Distances[5*HPCntMax+31]);
        printf("// i=%d  j=%d  dist=%f\n", 4, 30, HP_Distances[4*HPCntMax+30]);
        printf("// i=%d  j=%d  dist=%f\n", 3, 30, HP_Distances[3*HPCntMax+30]);
    */
    for (i=1; i<=lastHP; i++) {
        for(j=0; j<HPCntMax; j++) wa4[j] = 1;
        k = i * HPCntMax;
        // Create the set
        wa3[0] = i; pt = 1;
        wa4[i] = 0;

        for (j=1; j<=lastHP; j++) {
            if (wa4[j] && HP_Distances[k+j] <= dst) {
                wa3[pt++] = j; wa4[j] = 0;
            }
        }
        if (pt > 1) {
            // keep the configuration
            cf++;
            defC(cbase+cf, pt);
            //printf("%04d  %02d   ", cbase+cf, pt);
            for (k=0; k<pt; k++) {
               printf("%02d ", wa3[k]);
           }
           printf("   0\n");
        }
    }
}


// Compute points at some distance from a point
void mkset(int cbase, float px, float fx, float py, float fy,
        float pz, float fz, float dmin, float dmax)
{
    int i, k, pt;
    float d;
    pt = 0;
    for (i=1; i<=lastHP; i++) {
        d = sqrt((HP_x[i]-px)*(HP_x[i]-px)*fx + (HP_y[i]-py)*(HP_y[i]-py)*fy + 
                 (HP_z[i]-pz)*(HP_z[i]-pz)*fz);
        if ((d >= dmin) && (d <= dmax)) {
            // printf(" HP: %d   d -> %f  /  %f\n", i, d, fabs(HP_z[i]-pz));
            wa2[pt] = i; pt += 1;
        }
    }
    defC(cbase, pt);
    //printf("%04d  %02d   ", cbase, pt);
    for (k=0; k<pt; k++) {
        printf("%02d ", wa2[k]);
    }   
    printf("   0\n");

}


void sepline(char*txt)
{
    printf("\n//  %s\n", txt);
}


void prstats()
{
    int i, cfn, tsz, k;
    cfn = tsz = 0;
    for (i=0; i<CFdfsSiz; i++) {
        k = CFdfs[i];
        if (k != 0) cfn++;
        if (k > 0) tsz += k;
    }
    printf("\n//  Configurations: %d   Size: %d\n\n", cfn, tsz);
}

         

int main(int argc, char * argv[])
{
    int c, n, cbase;
    float hh, hd;

    // decode the parameters
    while ((c = getopt(argc, argv, "c:de:f:hi:l:p:s:t:v:x:z:")) > 0)
    {
        switch(c)
        {
            case '?':  // unrecognized option
                sprintf(msgerr, "Unknown option: \"%c\".", optopt);
                gerror(msgerr);
        }
    }



    bdHPpos();

    sepline("==========  AUTOMATED GENERATION START  ==========");


    cbase = 800;


    sepline("Points");
    // Chaque point
    mkpoints(HP_Proxim, cbase);
    cbase += 100;


    sepline("Distant points");
    // Les plus distants d'un point donné
    mkpoints(HP_Distant, cbase);
    cbase += 100;


    sepline("Horizontal Stereo pairs");
    lastCF = cbase + 1;
    for (n=1; n<=lastHP; n++) {
        mkpair(0, n, 0, 2, 0);
        mkpair(0, n, 0, -2, 0);
        mkpair(0, n, 2, 0, 0);
        mkpair(0, n, -2, 0, 0);
    }
    cbase += 100;

    sepline("Horizontal Large Stereo pairs");
    lastCF = cbase + 1;
    for (n=1; n<=lastHP; n++) {
        mkpair(0, n, 2, 2, 0);
        mkpair(0, n, 2, -2, 0);
        mkpair(0, n, -2, 2, 0);
        mkpair(0, n, -2, -2, 0);
    }
    cbase += 100;

    sepline("Near couples");
    // Couples les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 2);
    cbase += 100;

    sepline("Distant couples");
    // Couples les plus proches, les plus éloignés d'un point donné
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Distant, cbase, n, 2);
    cbase += 100;

    sepline("Special configurations");
    // Special configurations
    lastCF = cbase + 1;
    // Center top
    printf("// Center top\n");
    mkset(0, 3, 1, 3, 1, 3.4, 1, 0.1, 1.75);
    mkset(0, 3, 1, 3, 1, 3, 1, 0.1, 1.75);

    // Center top
    printf("// Center top+\n");
    mkset(0, 3, 1, 3, 1, 3, 1, 0.1, 2.25);

    printf("// Distant top\n");
    dfCnf2(0, 36, 40);

    // Roof top
    printf("// Roof top\n");
    mkset(0, 3, 0, 3, 0, 3, 1, 0, 0.8);

    // Greater roof top
    printf("// Greater roof top\n");
    mkset(0, 3, 0, 3, 0, 3, 1, 0.1, 1.1);

    // All but floor
    printf("// all but floor\n");
    mkset(0, 3, 0, 3, 0, 3, 1, 0.1, 2.5);

    // Main dome
    printf("// Main dome\n");
    mkset(0, 3, 1, 3, 1, 1, 1, 1.8, 4.8);


    // Coque 1 - y
    printf("// Y Coques\n");
    mkset(0, 3, 0, 6, 1, 1, 0, 0, 3.1);
    mkset(0, 3, 0, 0, 1, 1, 0, 0, 3.1);
    printf("// X Coques\n"); 
    mkset(0, 0, 1, 3, 0, 1, 0, 0, 3.1);
    mkset(0, 6, 1, 3, 0, 1, 0, 0, 3.1);
    printf("// Top Coques\n"); 
    mkset(0, 3, 1, 3, 1, 1.5, 1, 3.1, 7.1);
    mkset(0, 3, 1, 3, 1, 1.5, 1, 3.2, 7.1);
    mkset(0, 3, 1, 3, 1, 1.5, 1, 3.5, 7.1);
    mkset(0, 3, 1, 3, 1, 1.5, 1, 3.7, 7.1);
    mkset(0, 3, 1, 3, 1, 1.5, 1, 3.9, 7.1);
    printf("// Tranches\n");
    mkset(0, 3, 0, 3, 1, 1.5, 0, 0.0, 2.1);
    mkset(0, 3, 1, 3, 0, 1.5, 0, 0.0, 2.1);


    // Central cube
    printf("// Central blocks\n");
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 1.9); // 6
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 3.1); // 12
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 3.2); // 20
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 3.52); // 22
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 3.6); // 30
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 4.2); // 34
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 4.4); // 38
    mkset(0, 3, 1, 3, 1, 1.6, 1, 0.5, 4.6); // 42

    // Cubes
    printf("// small cubes\n");
    hh = (0 + h1val) / 2;
    hd = 2.3;
    mkset(0, 1, 1, 1, 1, hh, 1, 0.1, hd);
    mkset(0, 3, 1, 1, 1, hh, 1, 0.1, hd);
    mkset(0, 5, 1, 1, 1, hh, 1, 0.1, hd);
    mkset(0, 1, 1, 3, 1, hh, 1, 0.1, hd);
    mkset(0, 3, 1, 3, 1, hh, 1, 0.1, hd);
    mkset(0, 5, 1, 3, 1, hh, 1, 0.1, hd);
    mkset(0, 1, 1, 5, 1, hh, 1, 0.1, hd);
    mkset(0, 3, 1, 5, 1, hh, 1, 0.1, hd);
    mkset(0, 5, 1, 5, 1, hh, 1, 0.1, hd);
    printf("// large cubes\n");
    hh = h2val / 2;
    hd = 3.3;
    mkset(0, 2, 1, 2, 1, hh, 1, 0.1, hd);
    mkset(0, 2, 1, 4, 1, hh, 1, 0.1, hd);
    mkset(0, 4, 1, 2, 1, hh, 1, 0.1, hd);
    mkset(0, 4, 1, 4, 1, hh, 1, 0.1, hd);
    cbase += 100;

    sepline("Nearest 3 HPs");
    // Groupe de 3 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 3);
    cbase += 100;

    sepline("Nearest 4 HPs");
    // Groupe de 4 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 4);
    cbase += 100;

    sepline("Nearest 5 HPs");
    // Groupe de 5 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 5);
    cbase += 100;

    sepline("Nearest 6 HPs");
    // Groupe de 6 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 6);
    cbase += 100;

    sepline("Nearest 7 HPs");
    // Groupe de 7 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 7);
    cbase += 100;

    sepline("Nearest 8 HPs");
    // Groupe de 8 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 8);
    cbase += 100;

    sepline("Nearest 9 HPs");
    // Groupe de 9 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 9);
    cbase += 100;

    sepline("Nearest 13 HPs");
    // Groupe de 13 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 13);
    cbase += 100;

    sepline("Nearest 18 HPs");
    // Groupe de 18 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 18);
    cbase += 100;

    sepline("Nearest 24 HPs");
    // Groupe de 24 HP les plus proches
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 24);
    cbase += 100;

    
    sepline("Compact Blocks");
    // Quasi cubes
    mkqcu(cbase, 3.17);
    cbase += 100;

    sepline("Strait lines");
    // Les lignes droites
    printf("// y direction\n");
    mklines(cbase, 0, 1, 0);
    printf("// x direction\n");
    mklines(cbase + 20, 1, 0, 0);
    printf("// z direction\n");
    mklines(cbase + 40, 0, 0, 1);
    cbase += 100;

    sepline("Planes");
    // Les plans
    printf("// X-Y\n");
    mklines(cbase, 1, 1, 0);
    printf("// X-Z\n");
    mklines(cbase + 20, 1, 0, 1);
    printf("// Y-Z\n");
    mklines(cbase + 40, 0, 1, 1);
    cbase += 100;

    sepline("Proximity");
    // Classement par ordre de proximité
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Proxim, cbase, n, 42);
    cbase += 100;

    sepline("Distance");
    // Classement par éloignement
    for (n=1; n<=lastHP; n++)
        cnfprt(HP_Distant, cbase, n, 42);
    cbase += 100;

    prstats();

    sepline("==========  AUTOMATED GENERATION END  ==========\n");

    exit(0);
}


