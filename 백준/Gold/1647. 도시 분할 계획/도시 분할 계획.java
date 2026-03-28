import java.util.*;
import java.io.*;

public class Main {
    private static int[] parent;

    private static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }
        return parent[n];
    }

    private static void union(int u, int v) {
        int U = find(u);
        int V = find(v);
        if (u < v) parent[V] = U;
        else parent[U] = V;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        int[][] edges = new int[M][3];
        parent = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < M; i++) {
            inputs = br.readLine().split(" ");
            for (int j = 0; j < 3; j++) {
                edges[i][j] = Integer.parseInt(inputs[j]);
            }
        }
        Arrays.sort(edges, Comparator.comparingInt(a -> a[2]));

        int ans = 0, last = 0;
        for (int i = 0; i < M; i++) {
            int A = edges[i][0], B = edges[i][1], C = edges[i][2];
            if (find(A) != find(B)) {
                union(A, B);
                ans += C;
                last = C;
            }
        }
        bw.write(String.valueOf(ans - last));

        bw.flush();
        bw.close();
        br.close();
    }
}