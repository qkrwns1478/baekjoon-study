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
        int[] nm = getArray(2);
        int N = nm[0], M = nm[1];
        int[] A = getArray(N);
        int[] B = getArray(M);
        int ans = Arrays.stream(A).max().getAsInt() + Arrays.stream(B).max().getAsInt();
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}