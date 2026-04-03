import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] getArray() throws IOException {
        String[] inputs = br.readLine().split(" : ");
        int[] res = new int[3];
        for (int i = 0; i < 3; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    private static int getTime(int[] arr) {
        return arr[0] * 3600 + arr[1] * 60 + arr[2];
    }

    public static void main(String[] args) throws IOException {
        int[] S = getArray();
        int[] E = getArray();

        int timeS = getTime(S);
        int timeE = getTime(E);
        int ans = timeS > timeE ? 24 * 3600 - timeS + timeE : timeE - timeS;
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}