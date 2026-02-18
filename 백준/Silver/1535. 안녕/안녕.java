import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[][] arr = new int[N+1][2];
        int[][] dp = new int[N+1][100];
        for (int i = 0; i < 2; i++) {
            for (int j = 1; j <= N; j++) {
                arr[j][i] = scanner.nextInt();
            }
        }
        for (int i = 1; i <= N; i++) {
            int a = arr[i][0];
            int b = arr[i][1];
            for (int j = 1; j < 100; j++) {
                if (j >= a) {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-a] + b);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        System.out.println(dp[N][99]);
        scanner.close();
    }
}