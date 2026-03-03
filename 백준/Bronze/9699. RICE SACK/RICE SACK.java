import java.util.*;

public class Main {
    private static final int N = 5;
    private static final int[] arr = new int[N+1];
    private static final int[] tree = new int[N*4];

    private static void init(int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        init(node*2, start, mid);
        init(node*2+1, mid+1, end);
        tree[node] = Math.max(tree[node*2], tree[node*2+1]);
    }

    private static int query(int node, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return Integer.MIN_VALUE;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int l = query(node*2, start, mid, left, right);
        int r = query(node*2+1, mid+1, end, left, right);
        return Math.max(l, r);
    }

    private static void update(int node, int start, int end, int index, int value) {
        if (index < start || index > end) {
            return;
        }
        if (start == end) {
            arr[index] = value;
            tree[node] = value;
            return;
        }
        int mid = (start + end) / 2;
        update(node*2, start, mid, index, value);
        update(node*2+1, mid+1, end, index, value);
        tree[node] = Math.max(tree[node*2], tree[node*2+1]);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 1; t <= T; t++) {
            for (int i = 0; i < N; i++) {
                arr[i] = scanner.nextInt();
            }
            // int max = Arrays.stream(arr).max().getAsInt();
            init(1, 0, N-1);
            int max = query(1, 0, N-1, 0, N-1);
            System.out.printf("Case #%d: %d\n", t, max);
        }
        scanner.close();
    }
}