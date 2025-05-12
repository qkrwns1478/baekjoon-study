#include <stdio.h>
int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    if (n == 1 || m == 1) printf("0\n");
    else printf("%d\n", (n-1)*(m-1)*2);
    return 0;
}