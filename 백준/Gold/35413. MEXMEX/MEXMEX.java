import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        if (N == 1 && K == 2) {
            System.out.println(-1);
        } else {
            int[] A = new int[N];
            if (K > 0) {
                for (int i = 0; i < K-1; i++) {
                    A[i] = i;
                }
                for (int i = K-1; i < N; i++) {
                    A[i] = K;
                }
            }
            for (int i = 0; i < N; i++) {
                System.out.printf("%d ", A[i]);
            }
            System.out.println();
        }
        scanner.close();
    }
}