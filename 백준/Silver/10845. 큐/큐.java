import java.util.*;
import java.io.*;

public class Main {
    private static Queue<Integer> queue = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            switch (inputs[0]) {
                case "push" -> queue.add(Integer.parseInt(inputs[1]));
                case "pop" -> {
                    bw.write(!queue.isEmpty() ? String.valueOf(queue.poll()) : "-1");
                    bw.write("\n");
                }
                case "size" -> {
                    bw.write(String.valueOf(queue.size()));
                    bw.write("\n");
                }
                case "empty" -> {
                    bw.write(queue.isEmpty() ? "1" : "0");
                    bw.write("\n");
                }
                case "front" -> {
                    bw.write(!queue.isEmpty() ? String.valueOf(queue.peek()) : "-1");
                    bw.write("\n");
                }
                case "back" -> {
                    bw.write(!queue.isEmpty() ? String.valueOf(queue.toArray()[queue.size() - 1]) : "-1");
                    bw.write("\n");
                }
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}