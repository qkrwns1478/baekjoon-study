import java.io.*;
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
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        while (N-- > 0) {
            String[] inputs = br.readLine().split(" ");
            int Q = Integer.parseInt(inputs[0]);
            switch (Q) {
                case 1:
                    push(Integer.parseInt(inputs[1]));
                    break;
                case 2:
                    bw.write(pop() +"\n");
                    break;
                case 3:
                    bw.write(getSize() +"\n");
                    break;
                case 4:
                    bw.write(isEmpty() +"\n");
                    break;
                case 5:
                    bw.write(peek() +"\n");
                    break;
                default:
                    break;
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}