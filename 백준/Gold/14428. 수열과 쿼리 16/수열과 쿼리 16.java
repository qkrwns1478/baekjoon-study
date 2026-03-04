import java.util.*;

public class Main {
    private static int[] arr;
    private static int[] tree;

    private static int getMinIndex(int node) {
        if (arr[tree[node*2]] <= arr[tree[node*2+1]]) return tree[node*2];
        else return tree[node*2+1];
    }

    private static void init(int node, int start, int end) {
        if (start == end) {
            tree[node] = start;
            return;
        }
        int mid = (start + end) / 2;
        init(node*2, start, mid);
        init(node*2+1, mid+1, end);
        tree[node] = getMinIndex(node);
    }

    private static int query(int node, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return -1;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int index1 = query(node*2, start, mid, left, right);
        int index2 = query(node*2+1, mid+1, end, left, right);
        if (index1 == -1) return index2;
        else if (index2 == -1) return index1;
        else if (arr[index1] <= arr[index2]) return index1;
        else return index2;
    }

    private static void update(int node, int start, int end, int index, int value) {
        if (index < start || index > end) {
            return;
        }
        if (start == end) {
            arr[index] = value;
            tree[node] = index;
            return;
        }
        int mid = (start + end) / 2;
        update(node*2, start, mid, index, value);
        update(node*2+1, mid+1, end, index, value);
        tree[node] = getMinIndex(node);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        tree = new int[N*4];
        init(1, 0, N-1);
        int M = scanner.nextInt();
        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            if (a == 1) {
                update(1, 0, N-1, b-1, c);
            } else {
                int min = query(1, 0, N-1, b-1, c-1);
                System.out.println(min+1);
            }
        }
        scanner.close();
    }
}