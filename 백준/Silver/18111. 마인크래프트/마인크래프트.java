import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_HEIGHT = 256;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int B = Integer.parseInt(inputs[2]);
        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            inputs = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(inputs[j]);
            }
        }
        int TIME = Integer.MAX_VALUE, HEIGHT = 0;
        for (int h = 0; h <= MAX_HEIGHT; h++) {
            int u = 0, v = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (arr[i][j] > h) v += arr[i][j] - h;
                    else u += h - arr[i][j];
                }
            }
            if (u > v + B) continue;
            int cur = u + 2*v;
            if (cur <= TIME) {
                TIME = cur;
                HEIGHT = h;
            }
        }
        System.out.println(TIME + " " + HEIGHT);
        br.close();
    }
}