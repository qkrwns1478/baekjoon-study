#include <stdio.h>
#include <stdlib.h>
int compare(int* a, int* b) {
	return (*a - *b);
}
int main() {
  int a, b;
  scanf("%d %d", &a, &b);
  int *A = (int *)malloc(sizeof(int) * (a+b));
  for (int i = 0; i < a; i++) {
    scanf("%d", &A[i]);
  }
  for (int i = a; i < (a+b); i++) {
    scanf("%d", &A[i]);
  }
  qsort(A, a+b, sizeof(int), compare);
  for (int i = 0; i < (a+b); i++) {
    printf("%d ", A[i]);
  }
  free(A);
  return 0;
}