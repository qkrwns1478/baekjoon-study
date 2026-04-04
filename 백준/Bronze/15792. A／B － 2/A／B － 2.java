import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] getArray() throws IOException {
        String[] inputs = br.readLine().split(" ");
        int[] res = new int[2];
        for (int i = 0; i < 2; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        int[] arr = getArray();
        int a = arr[0], b = arr[1];
        bw.write((a / b) + ".");
        a = (a % b) * 10;
        for (int i = 0; i < 1000; i++) {
            bw.write(String.valueOf(a / b));
            a = (a % b) * 10;
        }

        bw.flush();
        bw.close();
        br.close();
    }
}