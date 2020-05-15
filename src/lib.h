#ifndef LIB_H
#define LIB_H

// in integrate.c:
int integrate(int T, double dt, int N, double **X, double **Y, double **Vx, double **Vy, const double G, const int sun_mass);

// in file extrafunc.c:
int alloc2D(double ***A, int n, int m);

int free2D(double **A);

void populate(double ***A, int n, int m);

#endif
