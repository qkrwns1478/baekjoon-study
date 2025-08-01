#include <stdio.h>
#define MIN(x, y) ((x < y) ? (x) : (y))
int main() {
    int n;
    scanf("%d",&n);
    int dp[50000];
    for(int i = 1; i <= n; i++){
        dp[i] = dp[i-1] + 1;
        for(int j = 1; j*j <= i; j++) {
            dp[i] = MIN(dp[i], dp[i - j*j] + 1);
        }
    }
    printf("%d\n", dp[n]);
    return 0;
}