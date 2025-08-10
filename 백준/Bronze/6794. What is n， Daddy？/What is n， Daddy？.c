#include <stdio.h>
int main() {
    int n, ans;
    scanf("%d", &n);
    if (n == 1 || n == 9 || n == 10) ans = 1;
    else if (n == 2 || n == 3 || n == 7 || n == 8) ans = 2;
    else ans = 3;
    printf("%d", ans);
    return 0;
}