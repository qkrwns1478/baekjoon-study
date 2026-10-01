import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        // Please write your code here.
        int answer = 0;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            int max = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    max = Math.max(max, dp[j]+1);
                }
            }
            dp[i] = max;
            answer = Math.max(answer, max);
        }

        System.out.println(answer);
    }
}