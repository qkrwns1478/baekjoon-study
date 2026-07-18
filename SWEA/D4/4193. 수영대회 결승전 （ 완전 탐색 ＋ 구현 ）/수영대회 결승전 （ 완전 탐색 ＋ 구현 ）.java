import java.util.*;

public class Solution {
    private static final Scanner sc = new Scanner(System.in);
    private static final int[] dx = {1, 0, -1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            System.out.println("#" + tc + " " + solution());
        }
        sc.close();
    }

    private static int solution() {
        int N = sc.nextInt();
        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int D = sc.nextInt();

        int answer = -1;
        Queue<Integer[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[N][N];
        queue.add(new Integer[]{A, B, 0});
        visited[A][B] = true;

        while(!queue.isEmpty()) {
            Integer[] cur = queue.poll();
            int x = cur[0], y = cur[1], t = cur[2];
            if (x == C && y == D) {
                answer = t;
                break;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                    if ((arr[nx][ny] == 0 || (arr[nx][ny] == 2 && t % 3 == 2)) && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.add(new Integer[]{nx, ny, t+1});
                    }
                }
            }
            if (t % 3 != 2) {
                queue.add(new Integer[]{x, y, t+1});
            }
        }

        return answer;
    }
}
