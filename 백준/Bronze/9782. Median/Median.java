import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int cnt = 0;
        while (N > 0) {
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = scanner.nextInt();
            }
            cnt++;
            double ans;
            if (N % 2 == 0) {
                ans = (double) (arr[N/2 - 1] + arr[N/2]) / 2;
            } else {
                ans = arr[(N-1)/2];
            }
            System.out.println("Case " + cnt + ": " + ans);
            N = scanner.nextInt();
        }
        scanner.close();
    }
}