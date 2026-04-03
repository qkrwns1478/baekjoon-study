import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            int M = Integer.parseInt(inputs[0]);
            int L1 = Integer.parseInt(inputs[1]);
            int L2 = Integer.parseInt(inputs[2]);
            int L3 = Integer.parseInt(inputs[3]);
            int total = L1 + L2 + L3;
            String res = total >= 55 && L1 >= 11 && L2 >= 8 && L3 >= 12 ? "PASS" : "FAIL";
            bw.write(String.valueOf(M) + " " + String.valueOf(total) + " " + res + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}