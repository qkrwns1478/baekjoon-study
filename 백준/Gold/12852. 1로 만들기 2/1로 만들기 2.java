import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N+1];
        StringBuilder[] sbs = new StringBuilder[N+1];
        sbs[1] = new StringBuilder("1");

        for (int i = 2; i < N+1; i++) {
            dp[i] = dp[i-1] + 1;
            int prev = i - 1;
            if (i % 3 == 0 && dp[i/3] + 1 < dp[i]) {
                dp[i] = dp[i/3] + 1;
                prev = i / 3;
            }
            if (i % 2 == 0 && dp[i/2] + 1 < dp[i]) {
                dp[i] = dp[i/2] + 1;
                prev = i / 2;
            }
            sbs[i] = new StringBuilder(String.valueOf(i) + " " + sbs[prev]);
        }

        bw.write(String.valueOf(dp[N]) + "\n");
        bw.write(String.valueOf(sbs[N]));

        bw.flush();
        bw.close();
        br.close();
    }
}