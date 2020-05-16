
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <errno.h>
#include "lib.h"

int main(int argc, char **argv) {
  MPI_Init(&argc, &argv);
  int rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  int N = atoi(argv[1]);
  double T = atoi(argv[2]);

  const double G = 4*M_PI*M_PI;
  const int sun_mass = 1;
  double dt = T / N;

  double X0[] = {0.466697, 0.7282, 1.0166426, 1.6660, 5.4588, 10.1238, 20.11, 30.33, 49.305};
  double Vy0[] = {8.16357231, 7.33666783, 6.18068911, 4.64079046, 2.62415606, 1.91749024, 1.36903319, 1.13277476, 0.782606028};

  double *X = malloc(N*sizeof(X));
  double *Y = malloc(N*sizeof(Y));
  double *Vx = malloc(N*sizeof(Vx));
  double *Vy = malloc(N*sizeof(Vy));

  printf("%lf %lf\n", G, dt);

  X[0] = X0[rank];
  Y[0] = 0.0;
  Vx[0] = 0.0;
  Vy[0] = Vy0[rank];

  integrate(T, dt, N, &X, &Y, &Vx, &Vy, G, sun_mass);

  free(Vx);
  free(Vy);

  if (rank == 0) {
    char *xfile = "X0.bin";
    char *yfile = "Y0.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 1) {
    char *xfile = "X1.bin";
    char *yfile = "Y1.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 2) {
    char *xfile = "X2.bin";
    char *yfile = "Y2.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 3) {
    char *xfile = "X3.bin";
    char *yfile = "Y3.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 4) {
    char *xfile = "X4.bin";
    char *yfile = "Y4.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 5) {
    char *xfile = "X5.bin";
    char *yfile = "Y5.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 6) {
    char *xfile = "X6.bin";
    char *yfile = "Y6.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 7) {
    char *xfile = "X7.bin";
    char *yfile = "Y7.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }
  if (rank == 8) {
    char *xfile = "X8.bin";
    char *yfile = "Y8.bin";
    write_to_file(xfile, X, N);
    write_to_file(yfile, Y, N);
  }

  free(X);
  free(Y);

  MPI_Finalize();

  return 0;
}
