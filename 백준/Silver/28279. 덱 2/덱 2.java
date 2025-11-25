import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    private static final LinkedList<Integer> deque = new LinkedList<>();
    private static BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int Q = Integer.parseInt(st.nextToken());
            solution(Q, st);
        }
        bw.flush();
        bw.close();
        br.close();
    }

    private static void solution(int query, StringTokenizer st) throws IOException {
        switch (query) {
            case 1:
                deque.addFirst(Integer.parseInt(st.nextToken()));
                break;
            case 2:
                deque.addLast(Integer.parseInt(st.nextToken()));
                break;
            case 3:
                bw.write((deque.isEmpty() ? -1 : deque.removeFirst()) + "\n");
                break;
            case 4:
                bw.write((deque.isEmpty() ? -1 : deque.removeLast()) + "\n");
                break;
            case 5:
                bw.write(deque.size() + "\n");
                break;
            case 6:
                bw.write((deque.isEmpty() ? 1 : 0) + "\n");
                break;
            case 7:
                bw.write((deque.isEmpty() ? -1 : deque.getFirst()) + "\n");
                break;
            case 8:
                bw.write((deque.isEmpty() ? -1 : deque.getLast()) + "\n");
                break;
        }
    }
}