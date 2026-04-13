import java.io.*;
import java.util.*;

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
        int[] arr = getArray(3);
        int k = arr[2];
        int[] score = new int[k+1];
        score[0] = Integer.MAX_VALUE;
        for (int i = 1; i <= k; i++) {
            arr = getArray(2);
            int f = arr[0], d = arr[1];
            score[i] = (f - 1) + (4 - d);
        }
        int min = Arrays.stream(score).min().getAsInt();
        for (int i = 1; i <= k; i++) {
            if (score[i] == min) {
                bw.write(String.valueOf(i));
                break;
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}