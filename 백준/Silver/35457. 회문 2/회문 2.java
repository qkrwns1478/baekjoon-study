import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int A = Integer.parseInt(br.readLine());
            bw.write(String.valueOf(A-1) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}