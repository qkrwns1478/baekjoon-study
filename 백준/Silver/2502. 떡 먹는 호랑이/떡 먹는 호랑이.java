import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int D = scanner.nextInt();
        int K = scanner.nextInt();
        long[] dp = new long[D];
        dp[0] = 1;
        dp[1] = 1;
        while (true) {
            for (int i = 2; i < D; i++) {
                dp[i] = dp[i-1] + dp[i-2];
            }
            if (dp[D-1] == K) {
                System.out.println(dp[0]);
                System.out.println(dp[1]);
                break;
            } else if (dp[D-1] > K) {
                dp[0]++;
                dp[1] = dp[0];
            } else {
                dp[1]++;
            }
        }
        scanner.close();
    }
}