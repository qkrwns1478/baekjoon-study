import java.io.*;
import java.util.*;

public class Main {
    private static double x1, y1, x2, y2, x3, y3, x4, y4;

    private static void sol() {
        double x, y;
        if (x1 == x3 && y1 == y3) {
            x = x2 + x4 - x1;
            y = y2 + y4 - y1;
        } else if (x1 == x4 && y1 == y4) {
            x = x2 + x3 - x1;
            y = y2 + y3 - y1;
        } else if (x2 == x3 && y2 == y3) {
            x = x1 + x4 - x2;
            y = y1 + y4 - y2;
        } else {
            x = x1 + x3 - x2;
            y = y1 + y3 - y2;
        }
        System.out.printf("%.3f %.3f\n", x, y);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while (true) {
            line = br.readLine();
            if (line == null) break;
            String[] inputs = line.split(" ");
            x1 = Double.parseDouble(inputs[0]);
            y1 = Double.parseDouble(inputs[1]);
            x2 = Double.parseDouble(inputs[2]);
            y2 = Double.parseDouble(inputs[3]);
            x3 = Double.parseDouble(inputs[4]);
            y3 = Double.parseDouble(inputs[5]);
            x4 = Double.parseDouble(inputs[6]);
            y4 = Double.parseDouble(inputs[7]);
            sol();
        }
        br.close();
    }
}