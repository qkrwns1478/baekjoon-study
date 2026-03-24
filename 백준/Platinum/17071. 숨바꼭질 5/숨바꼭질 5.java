import java.util.*;

public class Main {
    private static final int MAX = 500000;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{N, 0});
        boolean[][] visited = new boolean[MAX+1][2];
        visited[N][0] = true;
        int ans = -1;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int X = cur[0], T = cur[1];
            if (visited[K+(T*(T+1)/2)][T%2]) {
                ans = T;
                break;
            }
            visited[X][T%2] = true;
            if (K + (T+1)*(T+2)/2 <= MAX) {
                if (X-1 >= 0 && !visited[X-1][(T+1)%2]) {
                    visited[X-1][(T+1)%2] = true;
                    queue.add(new int[]{X-1, T+1});
                }
                if (X+1 <= MAX && !visited[X+1][(T+1)%2]) {
                    visited[X+1][(T+1)%2] = true;
                    queue.add(new int[]{X+1, T+1});
                }
                if (X*2 <= MAX && !visited[X*2][(T+1)%2]) {
                    visited[X*2][(T+1)%2] = true;
                    queue.add(new int[]{X*2, T+1});
                }
            }
        }
        System.out.println(ans);
        scanner.close();
    }
}