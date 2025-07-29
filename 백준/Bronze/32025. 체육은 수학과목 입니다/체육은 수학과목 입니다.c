#include <stdio.h>
#include <stdlib.h>
#define MIN(x, y) ((x < y) ? (x) : (y))
int main() {
  int h, w, a;
  scanf("%d", &h);
  scanf("%d", &w);
  a = MIN(h, w);
  int ans = (a * 100) / 2;
  printf("%d", ans);
  return 0;
}