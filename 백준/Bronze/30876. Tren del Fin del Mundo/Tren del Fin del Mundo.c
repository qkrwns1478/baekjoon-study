#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    int mx, my = 1001;
    for (int i = 0; i < n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        if (my > y) {
            mx = x;
            my = y;
        }
    }
    printf("%d %d\n", mx, my);
    return 0;
}