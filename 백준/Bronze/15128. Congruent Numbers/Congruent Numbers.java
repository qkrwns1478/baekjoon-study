import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static double[] getArray() throws IOException {
        String[] inputs = br.readLine().split(" ");
        double[] res = new double[4];
        for (int i = 0; i < 4; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        double[] arr = getArray();
        double a = arr[0] * arr[2];
        double b = arr[1] * arr[3] * 2;
        bw.write(String.valueOf(a % b == 0 ? 1 : 0));

        bw.flush();
        bw.close();
        br.close();
    }
}