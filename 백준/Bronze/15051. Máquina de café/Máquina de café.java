import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int[] A = new int[3];
        for (int i = 0; i < 3; i++) {
            A[i] = Integer.parseInt(br.readLine());
        }
        int min = Math.min(A[1] * 2 + A[2] * 4, A[0] * 2 + A[2] * 2);
        int ans = Math.min(min, A[0] * 4 + A[1] * 2);
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}