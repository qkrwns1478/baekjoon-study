import java.util.*;

public class Main {
    private static final int[] dx = {0, 0, -1, 1};
    private static final int[] dy = {1, -1, 0, 0};
    private static int N, M;
    private static int ans = Integer.MAX_VALUE;
    private static ArrayList<int[]> cameras;

    private static int[][] copyArray(int[][] arr) {
        int[][] res = new int[arr.length][];
        for (int i = 0; i < arr.length; i++) {
            res[i] = arr[i].clone();
        }
        return res;
    }

    private static void dfs(int[][] arr, int level) {
        if (level == cameras.toArray().length) {
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (arr[i][j] == 0) cnt++;
                }
            }
            ans = Math.min(ans, cnt);
            return;
        }

        int[][] dd;
        int[] cur = cameras.get(level);
        int type = cur[0], x = cur[1], y = cur[2];
        if (type == 1) {
            dd = new int[][]{{0}, {1}, {2}, {3}};
        } else if (type == 2) {
            dd = new int[][]{{0, 1}, {2, 3}};
        } else if (type == 3) {
            dd = new int[][]{{0, 2}, {0, 3}, {1, 3}, {1, 2}};
        } else if (type == 4) {
            dd = new int[][]{{0, 1, 2}, {0, 2, 3}, {0, 1, 3}, {1, 2, 3}};
        } else {
            dd = new int[][]{{0, 1, 2, 3}};
        }
        for (int i = 0; i < dd.length; i++) {
            int[][] newArr = copyArray(arr);
            for (int j = 0; j < dd[i].length; j++) {
                int nx = x + dx[dd[i][j]];
                int ny = y + dy[dd[i][j]];
                while (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    if (newArr[nx][ny] == 6) break;
                    newArr[nx][ny] = -1;
                    nx += dx[dd[i][j]];
                    ny += dy[dd[i][j]];
                }
            }
            dfs(newArr, level+1);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        int[][] A = new int[N][M];
        cameras = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int t = scanner.nextInt();
                A[i][j] = t;
                if (t != 0 && t != 6)
                    cameras.add(new int[]{t, i, j});
            }
        }

        dfs(A, 0);
        System.out.println(ans);
        scanner.close();
    }
}