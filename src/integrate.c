
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "lib.h"

double Ga(double X, double Y, const double G, const int sun_mass);

int integrate(int T, double dt, int N, double X[], double Y[], double Vx[], double Vy[], const double G, const int sun_mass) {
  double a1, a2, aa, dta1;

  for (size_t i = 0; i < N-1; i++) {
    a1 = Ga(X[i], Y[i], G, sun_mass)*dt*0.5;
    dta1 = a1*dt;
    X[i+1] = X[i] + dt*Vx[i] + dta1;
    Y[i+1] = Y[i] + dt*Vy[i] + dta1;

    a2 = Ga(X[i+1], Y[i+1], G, sun_mass)*dt*0.5;
    aa = a1+a2;
    Vx[i+1] = Vx[i] + aa;
    Vy[i+1] = Vy[i] + aa;

  }
  return 0;
}

double Ga(double X, double Y, const double G, const int sun_mass) {
  double r2 = X*X + Y*Y;
  return -G*sun_mass/r2;
}