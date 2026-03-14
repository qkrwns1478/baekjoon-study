import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        long[] dp = new long[N+1];
        dp[0] = 1;
        for (int i = 1; i < N+1; i++) {
            dp[i] = dp[i-1] * i;
        }
        System.out.println(dp[N] % 10);
        scanner.close();
    }
}