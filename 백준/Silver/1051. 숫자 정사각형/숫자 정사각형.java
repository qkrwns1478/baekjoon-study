import java.util.Scanner;

public class Main {
    static int N;
    static int M;
    static char[][] arr;

    private static boolean solution(int x) {
        for (int i = 0; i <= N-x; i++) {
            for (int j = 0; j <= M-x; j++) {
                if (arr[i][j] == arr[i+x-1][j] && arr[i][j] == arr[i][j+x-1] && arr[i][j] == arr[i+x-1][j+x-1]) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        arr = new char[N][M];
        for (int i = 0; i < N; i++) {
            String s = scanner.next();
            for (int j = 0; j < M; j++) {
                arr[i][j] = s.charAt(j);
            }
        }
        int ans = 1;
        for (int x = 2; x <= N; x++) {
            if (solution(x)) {
                ans = Math.max(ans, x*x);
            }
        }
        System.out.println(ans);
        scanner.close();
    }
}