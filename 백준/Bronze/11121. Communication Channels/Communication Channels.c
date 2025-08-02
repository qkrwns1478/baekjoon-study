#include <stdio.h>
#include <stdbool.h>
#include <string.h>
int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        char a[120];
        char b[120];
        scanf("%s %s", a, b);
        bool flag = true;
        int length = strlen(a);
        for (int j = 0; j < length; j++) {
            if (a[j] != b[j]) {
                flag = false;
                break;
            }
        }
        if (flag) printf("OK\n");
        else printf("ERROR\n");
    }
    return 0;
}