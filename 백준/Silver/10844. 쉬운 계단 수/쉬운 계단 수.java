import java.util.Scanner;

public class Main {
    public static final int MOD = 1000000000;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] dp = new int[n+1][10];
        for (int i = 1; i <= 9; i++) {
            dp[1][i] = 1;
        }
        for (int i = 2; i <= n; i++) {
            dp[i][0] = dp[i-1][1];
            for (int j = 1; j < 9; j++) {
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD;
            }
            dp[i][9] = dp[i-1][8];

        }
        System.out.println(getSum(dp[n]));

        scanner.close();
    }

    private static int getSum(int[] dp) {
        int result = 0;
        for (int i = 0; i <= 9; i++) {
            result = (result + dp[i]) % MOD;
        }
        return result;
    }
}