import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int Sab = Integer.parseInt(br.readLine());
        String[] inputs = br.readLine().split(" ");
        int Ma = Integer.parseInt(inputs[0]);
        int Fab = Integer.parseInt(inputs[1]);
        int Mb = Integer.parseInt(inputs[2]);

        if (Sab <= Ma + Fab + Mb || Sab <= 240) {
            bw.write("high speed rail");
        } else {
            bw.write("flight");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}