import java.io.*;
import java.util.*;

public class Main {
    private static int N, M;
    private static int[][] A;
    private static boolean[][][] visited;
    private static final int[] dx = {0, 1, 0, -1};
    private static final int[] dy = {1, 0, -1, 0};

    private static boolean dfs(int x, int y, int d) {
        if (0 <= x && x < N && 0 <= y && y < M) {
            if (!visited[x][y][d]) {
                visited[x][y][d] = true;
                return dfs(x+A[x][y]*dx[d], y+A[x][y]*dy[d], (d+1)%4);
            } else {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);
        A = new int[N][M];
        for (int i = 0; i < N; i++) {
            inputs = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(inputs[j]);
            }
        }

        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            visited = new boolean[N][M][4];
            if (dfs(i, 0, 0)) ans.add(i+1);
        }

        ans.sort(null);
        bw.write(String.valueOf(ans.size()) + "\n");
        for (Integer a: ans) {
            bw.write(String.valueOf(a) + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}