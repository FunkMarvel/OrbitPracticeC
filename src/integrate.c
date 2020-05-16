
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "lib.h"

double Ga(double X, double Y, const double G, const int sun_mass);

int integrate(int T, double dt, int N, double **X, double **Y, double **Vx, double **Vy, const double G, const int sun_mass) {
  double ax1, ay1, ax2, ay2, aa, dta1;

  for (size_t i = 0; i < N-1; i++) {
    ax1 = Ga((*X)[i], (*Y)[i], G, sun_mass)*dt*0.5;
    ay1 = Ga((*Y)[i], (*X)[i], G, sun_mass)*dt*0.5;

    dta1 = ax1*dt;
    (*X)[i+1] = (*X)[i] + dt*(*Vx)[i] + dta1;
    dta1 = ay1*dt;
    (*Y)[i+1] = (*Y)[i] + dt*(*Vy)[i] + dta1;

    ax2 = Ga((*X)[i+1], (*Y)[i+1], G, sun_mass)*dt*0.5;
    ay2 = Ga((*Y)[i+1], (*X)[i+1], G, sun_mass)*dt*0.5;
    aa = ax1+ax2;
    (*Vx)[i+1] = (*Vx)[i] + aa;
    aa = ay1+ay2;
    (*Vy)[i+1] = (*Vy)[i] + aa;

  }
  return 0;
}

double Ga(double x, double y, const double G, const int sun_mass) {
  double r2 = x*x + y*y;
  double unit = x / sqrt(r2);
  return -unit*G*sun_mass / r2;
}