import java.io.*;

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
        Cake A = new Cake(getNums());
        Cake C = new Cake(getNums());
        Cake B = new Cake(C.x - A.z, C.y / A.y, C.z - A.x);
        bw.write(B.x + " " + B.y + " " + B.z);

        bw.flush();
        bw.close();
        br.close();
    }
}