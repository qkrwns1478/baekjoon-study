import java.util.Scanner;

public class Main {
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] arr = new int[5][5];
    static int ans = Integer.MAX_VALUE;

    static void dfs(int cur, int cnt, int x, int y) {
        if (cnt == 3) {
            ans = Math.min(cur, ans);
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < 5 && 0 <= ny && ny < 5) {
                if (arr[nx][ny] == 1) {
                    arr[nx][ny] = -1;
                    dfs(cur+1, cnt+1, nx, ny);
                    arr[nx][ny] = 1;
                } else if (arr[nx][ny] == 0) {
                    arr[nx][ny] = -1;
                    dfs(cur+1, cnt, nx, ny);
                    arr[nx][ny] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = scanner.nextInt();
            }
        }
        int R = scanner.nextInt();
        int C = scanner.nextInt();
        arr[R][C] = -1;
        dfs(0, 0, R, C);
        if (ans == Integer.MAX_VALUE) ans = -1;
        System.out.println(ans);
        scanner.close();
    }
}