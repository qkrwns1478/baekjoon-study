import java.util.*;

public class Main {
    private static int N;
    private static int M;
    private static int[][] arr;
    private static boolean[][][] visited;
    private static final int[] dx = {0, 0, 0, 1, -1};
    private static final int[] dy = {0, 1, -1, 0, 0};

    private static int rotate(int d, boolean left) {
        if (d == 1) return left ? 4 : 3;
        else if (d == 2) return left ? 3 : 4;
        else if (d == 3) return left ? 1 : 2;
        else if (d == 4) return left ? 2 : 1;
        else return 0;
    }

    private static int[] turn(int x, int y, int d, boolean left) {
        int nd = rotate(d, left);
        if (!visited[x][y][nd]) return new int[]{1, nd};
        else return new int[]{0, 0};
    }

    private static int[] go(int x, int y, int d, int k) {
        int nx = x, ny = y;
        for (int i = 0; i < k; i++) {
            nx += dx[d];
            ny += dy[d];
            if (!(1 <= nx && nx <= N && 1 <= ny && ny <= M) || arr[nx][ny] == 1)
                return new int[]{0, 0, 0};
        }
        if (!visited[nx][ny][d]) return new int[]{1, nx, ny};
        else return new int[]{0, 0, 0};
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        arr = new int[N+1][M+1];
        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < M+1; j++) {
                arr[i][j] = scanner.nextInt();
            }
        }
        int sx = scanner.nextInt();
        int sy = scanner.nextInt();
        int sd = scanner.nextInt();
        int ex = scanner.nextInt();
        int ey = scanner.nextInt();
        int ed = scanner.nextInt();

        Deque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[] {sx, sy, sd, 0});
        visited = new boolean[N+1][M+1][5];
        visited[sx][sy][sd] = true;

        while (!queue.isEmpty()) {
            int[] pop = queue.removeFirst();
            int x = pop[0], y = pop[1], d = pop[2], q = pop[3];
            if (x == ex && y == ey && d == ed) {
                System.out.println(q);
                break;
            }
            // Go k
            for (int k = 3; k > 0; k--) {
                int[] res = go(x, y, d, k);
                if (res[0] == 1) {
                    int nx = res[1], ny = res[2];
                    visited[nx][ny][d] = true;
                    queue.addLast(new int[]{nx, ny, d, q+1});
                }
            }
            // Turn dir
            for (int l = 1; l >= 0; l--) {
                boolean left = l == 1;
                int[] res = turn(x, y, d, left);
                if (res[0] == 1) {
                    int nd = res[1];
                    visited[x][y][nd] = true;
                    queue.addLast(new int[]{x, y, nd, q+1});
                }
            }
        }

        scanner.close();
    }
}