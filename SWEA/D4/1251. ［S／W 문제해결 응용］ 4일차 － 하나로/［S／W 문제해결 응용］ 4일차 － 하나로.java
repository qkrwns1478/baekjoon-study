import java.util.*;

class Edge implements Comparable<Edge> {
    int from;
    int to;
    long weight;

    public Edge(int from, int to, long weight) {
        this.from = from;
        this.to = to;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge o) {
        return Long.compare(this.weight, o.weight);
    }
}

public class Solution {
    private static int[] root;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int t = 1; t <= T; t++) {
            int N = sc.nextInt();
            int[] X = new int[N];
            int[] Y = new int[N];
            for (int i = 0; i < N; i++) {
                X[i] = sc.nextInt();
            }
            for (int i = 0; i < N; i++) {
                Y[i] = sc.nextInt();
            }
            double E = sc.nextDouble();

            List<Edge> edgeList = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                for (int j = i+1; j < N; j++) {
                    long dx = X[i] - X[j];
                    long dy = Y[i] - Y[j];
                    long distSquare = dx * dx + dy * dy;
                    edgeList.add(new Edge(i, j, distSquare));
                }
            }
            Collections.sort(edgeList);

            root = new int[N];
            for (int i = 0; i < N; i++) {
                root[i] = i;
            }

            double total = 0;
            int cnt = 0;
            for (Edge e: edgeList) {
                if (union(e)) {
                    total += e.weight;
                    cnt++;
                    if (cnt == N-1) break;
                }
            }

            System.out.printf("#%d %d\n", t, Math.round(total * E));
        }

        sc.close();
    }

    private static boolean union(Edge e) {
        int rootA = find(e.from);
        int rootB = find(e.to);
        if (rootA == rootB)
            return false;
        root[rootB] = rootA;
        return true;
    }

    private static int find(int x) {
        if (root[x] == x) return x;
        else return root[x] = find(root[x]);
    }
}
