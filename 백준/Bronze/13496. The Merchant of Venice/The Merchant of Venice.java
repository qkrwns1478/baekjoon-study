import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int K = Integer.parseInt(br.readLine());
        for (int i = 1; i <= K; i++) {
            String[] inputs = br.readLine().split(" ");
            int N = Integer.parseInt(inputs[0]);
            int S = Integer.parseInt(inputs[1]);
            int D = Integer.parseInt(inputs[2]);
            int ans = 0;
            for (int j = 0; j < N; j++) {
                inputs = br.readLine().split(" ");
                int di = Integer.parseInt(inputs[0]);
                int vi = Integer.parseInt(inputs[1]);
                if (S * D >= di) ans += vi;
            }
            bw.write("Data Set " + i + ":\n" + ans + "\n\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}