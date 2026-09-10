import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        int[] dp = new int[n+1];
        if (n <= 4) {
            System.out.println(1);
            return;
        }
        for (int i = 2; i <= 4; i++) dp[i] = 1;
        for (int i = 5; i <= n; i++) dp[i] = (dp[i-2] + dp[i-3]) % 10007;
        System.out.println(dp[n]);
    }
}