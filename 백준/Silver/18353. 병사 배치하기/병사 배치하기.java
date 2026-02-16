import java.util.Scanner;
import static java.lang.Math.max;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        int[] dp = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
            dp[i] = 1;
        }
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (A[i] < A[j])
                    dp[i] = max(dp[i], dp[j]+1);
            }
        }
        int maxVal = 0;
        for (int i = 0; i < N; i++) {
            maxVal = max(maxVal, dp[i]);
        }
        System.out.println(N - maxVal);
        scanner.close();
    }
}