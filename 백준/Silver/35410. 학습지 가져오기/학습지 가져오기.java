import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        Arrays.sort(A);
        int ans = 0;
        for (int i = 0; i < N; i++) {
            ans = Math.max(ans, A[i]) + 1;
        }
        System.out.println(ans);
        scanner.close();
    }
}