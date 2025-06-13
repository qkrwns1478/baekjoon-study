#include <stdio.h>
#include <stdlib.h>
int main() {
    int n;
    scanf("%d", &n);

    char *str = (char *)malloc(sizeof(char) * (n+1));
    scanf("%s", str);
    
    long long tmp = 0;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if ((str[i] >= '0' && str[i] <= '9')) {
            tmp *= 10;
            tmp += str[i] - '0';
        } else {
            ans += tmp;
            tmp = 0;
        }
    }
    if (tmp != 0)
        ans += tmp;
    printf("%lld\n", ans);

    free(str);
    return 0;
}