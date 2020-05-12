
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "lib.h"

int main(int argc, char const *argv[]) {
  int N = atoi(argv[1]);
  int T = atoi(argv[2]);

  const double G = 4*M_PI*M_PI;
  double x0 = 1.00000102;
  double y0 = 0.0;
  double vx0 = 0.0;
  double vy0 = 6.28;
  const int sun_mass = 1;
  double dt = (double) T / N;
  printf("%lf %lf %lf %lf %lf %lf\n", G, x0, y0, vx0, vy0, dt);

  integrate(T, dt, N, x0, y0, vx0, vy0, G, sun_mass);

  return 0;
}
