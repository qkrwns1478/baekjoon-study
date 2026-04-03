import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        double X = Double.parseDouble(br.readLine());
        double ans = 100.0 / (X * (1.609344 / 3.785411784));
        bw.write(String.format("%.6f", ans));

        bw.flush();
        bw.close();
        br.close();
    }
}