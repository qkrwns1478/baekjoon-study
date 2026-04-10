import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] getArray(int n) throws IOException {
        String[] inputs = br.readLine().split(" ");
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        int[] inputs = getArray(3);
        int N = inputs[0], X = inputs[1], M = inputs[2];
        int[] crates = new int[N+1];
        crates[0] = 1001;
        for (int i = 0; i < M; i++) {
            crates[Integer.parseInt(br.readLine())]++;
        }

        int A = 0, B = 0;
        int pos = 1;
        while(pos < X) {
            A += crates[pos];
            pos++;
        }
        pos = N;
        while(pos >= X) {
            B += crates[pos];
            pos--;
        }
        // bw.write(A + " " + B + "\n");
        bw.write(String.valueOf(Math.min(A, B)));

        bw.flush();
        bw.close();
        br.close();
    }
}