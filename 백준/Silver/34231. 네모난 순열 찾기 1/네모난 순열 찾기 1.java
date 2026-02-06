import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[][] A = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = scanner.nextInt();
            }
        }
        int ans = 0;
        for (int x1 = 0; x1 < N; x1++) {
            for (int y1 = 0; y1 < N; y1++) {
                for (int x2 = x1; x2 < N; x2++) {
                    for (int y2 = y1; y2 < N; y2++) {
                        ans += sol(A, x1, y1, x2, y2);
                    }
                }
            }
        }
        System.out.println(ans);
        scanner.close();
    }

    private static int sol(int[][] arr, int sx, int sy, int ex, int ey) {
        Set<Integer> tmp = new HashSet<>();
        for (int i = sx; i <= ex; i++) {
            for (int j = sy; j <= ey; j++) {
                int num = arr[j][i];
                if (tmp.contains(num)) {
                    return 0;
                }
                tmp.add(num);
            }
        }
        int area = (Math.abs(sx - ex) + 1) * (Math.abs(sy - ey) + 1);
        for (int k = 1; k <= area; k++) {
            if (!tmp.contains(k)) {
                return 0;
            }
        }
        return 1;
    }
}
