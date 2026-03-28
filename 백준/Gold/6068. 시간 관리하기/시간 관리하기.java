import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[][] A = new int[N][2];
        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            for (int j = 0; j < 2; j++) {
                A[i][j] = Integer.parseInt(inputs[j]);
            }
        }
        Arrays.sort(A, (a, b) -> b[1] - a[1]);

        int ans = A[0][1];
        for (int i = 0; i < N; i++) {
            int S = A[i][0];
            int E = A[i][1];
            if (ans >= E) ans = E - S;
            else ans -= S;
        }
        bw.write(ans >= 0 ? String.valueOf(ans) : "-1");

        bw.flush();
        bw.close();
        br.close();
    }
}