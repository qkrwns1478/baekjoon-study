import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            if (N % 2 != 0) bw.write("0");
            else {
                long cur = 1;
                for (int j = 0; j < N / 2; j++) {
                    cur *= 2;
                }
                bw.write(String.valueOf(cur));
            }
            if (i != T-1) {
                bw.write("\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}