import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] getNums() throws IOException {
        String[] inputs = br.readLine().split(" ");
        int[] res = new int[3];
        for (int i = 0; i < 3; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        int[] A = getNums();
        int[] R = getNums();

        int ans = 0;
        for (int i = 0; i < 3; i++) {
            if (A[i] < R[i]) ans += R[i] - A[i];
        }
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}