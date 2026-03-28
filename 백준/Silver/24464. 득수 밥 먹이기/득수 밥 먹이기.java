import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        long[][] dp = new long[5][N];
        int MOD = 1000000007;

        for (int i = 0; i < 5; i++) {
            dp[i][0] = 1;
        }
        for (int j = 1; j < N; j++) {
            for (int i = 1; i < 5; i++) {
                dp[0][j] = (dp[0][j] + dp[i][j-1]) % MOD;
                for (int k = 0; k < 5; k++) {
                    if (k == 0 || k-i > 1 || k-i < -1) {
                        dp[i][j] = (dp[i][j] + dp[k][j-1]) % MOD;
                    }
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < 5; i++) {
            ans += dp[i][N-1];
        }
        bw.write(String.valueOf(ans % MOD));

        bw.flush();
        bw.close();
        br.close();
    }
}