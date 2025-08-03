#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        int p;
        long long q;
        scanf("%d %lld", &p, &q);

        long long dp[10001]; 
        dp[0] = 1 % q;
        dp[1] = 1 % q;
        dp[2] = 2 % q;

        for (int j = 3; j < p; j++) {
            dp[j] = (dp[j-1] + dp[j-2]) % q;
        }
        
        printf("Case #%d: %lld\n", i+1, dp[p-1]);
    }
    
    return 0;
}