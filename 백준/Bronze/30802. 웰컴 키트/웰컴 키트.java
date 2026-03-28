import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[6];
        String[] inputs = br.readLine().split(" ");
        for (int i = 0; i < 6; i++) {
            A[i] = Integer.parseInt(inputs[i]);
        }
        inputs = br.readLine().split(" ");
        int T = Integer.parseInt(inputs[0]);
        int P = Integer.parseInt(inputs[1]);
        int ans = 0;
        for (int i = 0; i < 6; i++) {
            ans += (A[i] % T == 0) ? (A[i] / T) : (A[i] / T + 1);
        }
        bw.write(ans + "\n");
        bw.write((N / P) + " " + (N % P) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}