import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static class Cake {
        int x, y, z;

        public Cake(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public Cake(int[] arr) {
            this.x = arr[0];
            this.y = arr[1];
            this.z = arr[2];
        }
    }

    private static int[] getNums() throws IOException {
        String[] inputs = br.readLine().split(" ");
        int[] res = new int[3];
        for (int i = 0; i < 3; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws Exception {
        int[] A = getNums();
        int[] C = getNums();
        Cake cakeA = new Cake(A);
        Cake cakeC = new Cake(C);

        Cake cakeB = new Cake(cakeC.x - cakeA.z, cakeC.y / cakeA.y, cakeC.z - cakeA.x);
        bw.write(cakeB.x + " " + cakeB.y + " " + cakeB.z);

        bw.flush();
        bw.close();
        br.close();
    }
}