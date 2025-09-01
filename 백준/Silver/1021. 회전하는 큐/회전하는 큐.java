import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        String[] arrStr = scanner.nextLine().split(" ");
        int[] arr = new int[m];
        for (int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(arrStr[i]);
        }

        Deque<Integer> dq = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            dq.addLast(i);
        }

        int answer = 0;
        int t = 0;

        while (t < m) {
            if (dq.peekFirst() == arr[t]) {
                dq.removeFirst();
                t++;
            } else {
                int targetIndex = ((LinkedList<Integer>) dq).indexOf(arr[t]);
                if (targetIndex <= dq.size() / 2) {
                    dq.addLast(dq.removeFirst());
                } else {
                    dq.addFirst(dq.removeLast());
                }
                answer++;
            }
        }
        System.out.println(answer);
    }
}