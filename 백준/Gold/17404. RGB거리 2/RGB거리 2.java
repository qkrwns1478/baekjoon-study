import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = 3;
        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = scanner.nextInt();
            }
        }

        int ans = Integer.MAX_VALUE;
        for (int j = 0; j < M; j++) {
            int[][] dp = new int[N][M];
            for (int k = 0; k < M; k++) {
                if (j == k) dp[0][k] = arr[0][j];
                else dp[0][k] = 1001;
            }
            for (int i = 1; i < N; i++) {
                dp[i][0] = arr[i][0] + Math.min(dp[i-1][1], dp[i-1][2]);
                dp[i][1] = arr[i][1] + Math.min(dp[i-1][0], dp[i-1][2]);
                dp[i][2] = arr[i][2] + Math.min(dp[i-1][0], dp[i-1][1]);
            }
            for (int i = 0; i < M; i++) {
                if (j != i) ans = Math.min(ans, dp[N-1][i]);
            }
        }

        System.out.println(ans);
        scanner.close();
    }
}