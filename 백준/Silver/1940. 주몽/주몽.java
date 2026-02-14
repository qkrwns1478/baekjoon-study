import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        Arrays.sort(A);

        int l = 0, r = N - 1;
        int ans = 0;
        while (l < r) {
            if (A[l] + A[r] >= M) {
                if (A[l] + A[r] == M) {
                    ans++;
                }
                r--;
            } else {
                l++;
            }
        }
        System.out.println(ans);
        scanner.close();
    }
}