#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include "lib.h"

int write_to_file(const char *filename, double *A, int N){
  FILE *pFile;

  pFile = fopen(filename, "wb+");
  if(pFile == NULL){
      perror("Error Occurred");
      printf("Error Code: %d\n", errno);
      exit(1);
  }
  fwrite(A, sizeof(A[0]), N, pFile);
  fclose(pFile);

  return 0;
}