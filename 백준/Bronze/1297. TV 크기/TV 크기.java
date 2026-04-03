import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int D = Integer.parseInt(inputs[0]);
        int H = Integer.parseInt(inputs[1]);
        int W = Integer.parseInt(inputs[2]);

        double R = (double) D / Math.sqrt(Math.pow(H, 2) + Math.pow(W, 2));
        int rH = (int) Math.floor(R * H);
        int rW = (int) Math.floor(R * W);
        bw.write(String.valueOf(rH) + " " + String.valueOf(rW));

        bw.flush();
        bw.close();
        br.close();
    }
}