#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long dp[51];
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= 50; i++) {
        dp[i] = dp[i-2] + dp[i-1] + 1;
    }
    
    printf("%d\n", dp[n] % 1000000007);

    return 0;
}