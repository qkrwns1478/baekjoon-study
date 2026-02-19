import java.util.Scanner;

public class Main {
    private static int max(int a, int b, int c) {
        int ab = Math.max(a, b);
        int bc = Math.max(b, c);
        return Math.max(ab, bc);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        int[] dp1 = new int[N];
        int[] dp2 = new int[N];
        int[] dp3 = new int[N];
        dp1[0] = arr[0];
        for (int i = 1; i < N; i++) {
            dp1[i] = dp2[i-1] + arr[i];
            dp2[i] = max(dp1[i-1], dp2[i-1], dp3[i-1]);
            dp3[i] = dp1[i-1] + arr[i] / 2;
        }
        System.out.println(max(dp1[N-1], dp2[N-1], dp3[N-1]));
        scanner.close();
    }
}