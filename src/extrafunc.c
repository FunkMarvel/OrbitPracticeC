// Extra functions for the two programs.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "lib.h"

// function for allocating contiguous matrix:
int alloc2D(double ***A, int n, int m)
{
    *A = malloc(n * sizeof *A);
    (*A)[0] = malloc(n*m * sizeof (*A)[0]);
    if (!(*A)[0] || !*A){   // warning if allocation failes:
        printf("Allocation failed\n");
        exit(1);
    }

    for (size_t i = 1; i < n; i++) {  // setting up pointers:
        (*A)[i] = &((*A)[0][i*m]);
    }
    return 0;
}


// function for freeing contiguous matrix:
int free2D(double **A)
{
    free(A[0]);
    free(A);
    return 0;
}

// function for populating NxM-matrix with pseudo-random numbers in range [0,10]:
void populate(double ***A, int n, int m) {
  srand(time(NULL));    // seeding rand().

  // populating matrix:
  for (size_t i = 0; i < n; i++) {
    for (size_t j = 0; j < m; j++) {
      (*A)[i][j] = rand() % 9;
    }
  }
}