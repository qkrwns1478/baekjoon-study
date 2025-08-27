import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int n;
    static int m;
    static int[][] arr;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();

        arr = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                arr[i][j] = scanner.nextInt();
            }
        visited = new boolean[n+1];
        int[] path = new int[m];
        for (int i = 0; i < m; i++) {
            path[i] = scanner.nextInt();
        }

        search(path[0] - 1);

        String res = "YES";
        for (int p : path) {
            if (!visited[p-1]) {
                res = "NO";
                break;
            }
        }
        System.out.println(res);
        scanner.close();
    }

    private static void search(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);  // push
        visited[start] = true;

        while (!q.isEmpty()) {
            int now = q.poll(); // pop
            for (int i = 0; i < n; i++) {
                if (arr[now][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.offer(i); // push
                }
            }
        }
    }
}