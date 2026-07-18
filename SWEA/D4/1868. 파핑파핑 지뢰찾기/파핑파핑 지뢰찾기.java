import java.util.*;

public class Solution {
    private static final Scanner sc = new Scanner(System.in);
    private static final int[] dx = {1, 0, -1, 0, 1, 1, -1, -1};
    private static final int[] dy = {0, 1, 0, -1, 1, -1, 1, -1};

    public static void main(String[] args) {
        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            System.out.println("#" + tc + " " + solution());
        }
        sc.close();
    }

    private static int N;
    private static char[][] arr;
    private static int[][] map;
    private static boolean[][] visited;

    private static int solution() {
        N = sc.nextInt();
        sc.nextLine();
        arr = new char[N][N];
        for (int i = 0; i < N; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < N; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        map = new int[N][N];
        visited = new boolean[N][N];
        ArrayList<Integer[]> zeros = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == '*') {
                    map[i][j] = -1;
                    continue;
                }
                int tmp = 0;
                for (int k = 0; k < 8; k++) {
                    int ni = i + dx[k];
                    int nj = j + dy[k];
                    if (isValid(ni, nj) && arr[ni][nj] == '*') tmp++;
                }
                map[i][j] = tmp;
                if (tmp == 0) zeros.add(new Integer[]{i, j});
            }
        }

        int answer = 0;
        for (Integer[] zero: zeros) {
            int x = zero[0], y = zero[1];
            if (!visited[x][y]) {
                dfs(x, y);
                answer++;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j] && arr[i][j] == '.') {
                    dfs(i, j);
                    answer++;
                }
            }
        }

        return answer;
    }

    private static void dfs(int x, int y) {
        visited[x][y] = true;
        if (map[x][y] == 0) {
            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (isValid(nx, ny) && arr[nx][ny] == '.' && !visited[nx][ny]) {
                    dfs(nx, ny);
                }
            }
        }
    }

    private static boolean isValid(int x, int y) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }
}
