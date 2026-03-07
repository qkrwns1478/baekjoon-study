import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final LinkedList<Integer> stack = new LinkedList<>();

    private static void push(int x) {
        stack.add(x);
    }

    private static int pop() {
        if (isEmpty() == 1) return -1;
        int res = stack.getLast();
        stack.removeLast();
        return res;
    }

    private static int getSize() {
        return stack.size();
    }

    private static int isEmpty() {
        return stack.isEmpty() ? 1 : 0;
    }

    private static int peek() {
        if (isEmpty() == 1) return -1;
        else return stack.getLast();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        while (N-- > 0) {
            String[] inputs = br.readLine().split(" ");
            int Q = Integer.parseInt(inputs[0]);
            switch (Q) {
                case 1:
                    int X = Integer.parseInt(inputs[1]);
                    push(X);
                    break;
                case 2:
                    System.out.println(pop());
                    break;
                case 3:
                    System.out.println(getSize());
                    break;
                case 4:
                    System.out.println(isEmpty());
                    break;
                case 5:
                    System.out.println(peek());
                    break;
                default:
                    break;
            }
        }
        br.close();
    }
}