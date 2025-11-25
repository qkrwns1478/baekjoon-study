import java.util.ArrayList;
import java.util.Stack;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        ArrayList<Integer> arr = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            arr.add(scanner.nextInt());
        }
        Stack<Integer> stack = new Stack<>();
        int x = 1;
        int idx = 0;
        while (idx < N) {
            int cur = arr.get(idx);
            int top = !stack.isEmpty() ? stack.peek() : -1;
            // System.out.printf("DEBUG: x=%d, cur=%d, top=%d\n", x, cur, top);
            if (cur == x) {
                x++;
                idx++;
            } else if (!stack.isEmpty() && top == x) {
                stack.pop();
                x++;
            } else {
                stack.push(cur);
                idx++;
            }
        }
        while (!stack.isEmpty()) {
            if (stack.peek() == x) {
                stack.pop();
                x++;
            } else {
                break;
            }
        }
        if (!stack.isEmpty()) {
            System.out.println("Sad");
        } else {
            System.out.println("Nice");
        }
        scanner.close();
    }
}