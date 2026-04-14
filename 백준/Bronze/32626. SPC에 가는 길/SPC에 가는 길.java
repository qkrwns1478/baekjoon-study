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
        int[] S = getArray(2);
        int[] E = getArray(2);
        int[] P = getArray(2);
        int sx = S[0], sy = S[1];
        int ex = E[0], ey = E[1];
        int px = P[0], py = P[1];

        boolean con1 = (py > sy && py < ey) || (py > ey && py < sy);
        boolean con2 = (px > sx && px < ex) || (px > ex && px < sx);
        boolean con3 = px == sx && con1;
        boolean con4 = py == sy && con2;
        int ans = sx == ex ? (con3 ? 2 : 0) : sy == ey ? (con4 ? 2 : 0) : 1;
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}