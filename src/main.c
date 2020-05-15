
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "lib.h"

int main(int argc, char const *argv[]) {
  int N = atoi(argv[1]);
  double T = atoi(argv[2]);

  const double G = 4*M_PI*M_PI;
  const int sun_mass = 1;
  double dt = T / N;

  double x0 = 1.00000102;
  double y0 = 0.0;
  double vx0 = 0.0;
  double vy0 = 6.28;

  double *X = malloc(N*sizeof(X));
  double *Y = malloc(N*sizeof(Y));
  double *Vx = malloc(N*sizeof(Vx));
  double *Vy = malloc(N*sizeof(Vy));

  printf("%lf %lf %lf %lf %lf %lf\n", G, x0, y0, vx0, vy0, dt);

  X[0] = x0;
  Y[0] = y0;
  Vx[0] = vx0;
  Vy[0] = vy0;

  integrate(T, dt, N, &X, &Y, &Vx, &Vy, G, sun_mass);
  for (size_t i = 0; i < 4; i++) {
    printf("(%lf,%lf)\n", X[i],Y[i]);
    printf("[%lf,%lf]\n", Vx[i],Vy[i]);
  }

  free(X);
  free(Y);
  free(Vx);
  free(Vy);

  return 0;
}
