import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] getArray(int n) throws IOException {
        String[] inputs = br.readLine().split(" ");
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        int mA = 0, mB = 0, eA = 0, eB = 0;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int[] arr = getArray(3);
            mA += arr[1];
            mB += arr[2];
            if (arr[1] > arr[2]) eA += arr[0];
            else if (arr[1] < arr[2]) eB += arr[0];
        }
        int ans = mA > mB && eA > eB ? 1 : mA < mB && eA < eB ? 2 : 0;
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}