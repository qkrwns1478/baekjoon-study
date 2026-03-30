import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int[] A = new int[N];
        inputs = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(inputs[i]);
        }

        long[] mods = new long[M];
        int S = 0;
        for (int i = 0; i < N; i++) {
            S = (S + A[i]) % M;
            mods[S]++;
        }

        long ans = mods[0];
        for (int i = 0; i < M; i++) {
            ans += mods[i] * (mods[i] - 1) / 2;
        }
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}