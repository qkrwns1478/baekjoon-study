import java.util.*;

public class Main {
    private static final int[] dx = {1, 0, -1, 0};
    private static final int[] dy = {0, 1, 0, -1};
    private static int N;
    private static int M;
    private static int[][] A;
    private static Set<String> outer;
    private static boolean[][] visited;
    private static Set<String> melt;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        A = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                A[i][j] = scanner.nextInt();
            }
        }

        int time = 0;
        while (true) {
            outer = new HashSet<>();
            Queue<int[]> queue = new ArrayDeque<>();
            visited = new boolean[N][M];
            outer.add("0,0");
            queue.add(new int[]{0, 0});
            visited[0][0] = true;

            // 치즈 바깥 공기 범위 먼저 구하기 (BFS)
            while (!queue.isEmpty()) {
                int[] cur = queue.poll();
                int x = cur[0], y = cur[1];
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i], ny = y + dy[i];
                    if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                        if (A[nx][ny] == 0 && !visited[nx][ny]) {
                            outer.add(nx + "," + ny);
                            queue.add(new int[]{nx, ny});
                            visited[nx][ny] = true;
                        }
                    }
                }
            }
            if (outer.size() == N * M)
                break;

            // 다음에 녹을 치즈 범위 구하기 (DFS)
            melt = new HashSet<>();
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (A[i][j] == 1 && !visited[i][j]) {
                        visited[i][j] = true;
                        dfs(i, j);
                    }
                }
            }

            // 치즈 녹이기
            for (String m: melt) {
                String[] cur = m.split(",");
                int x = Integer.parseInt(cur[0]);
                int y = Integer.parseInt(cur[1]);
                A[x][y] = 0;
            }
            time++;
        }
        
        System.out.println(time);
        scanner.close();
    }

    private static void dfs(int x, int y) {
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (outer.contains(nx + "," + ny)) {
                    cnt++;
                }
            }
        }
        if (cnt >= 2)
            melt.add(x + "," + y);
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (A[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    dfs(nx, ny);
                }
            }
        }
    }
}