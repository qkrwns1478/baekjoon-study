import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static class Rocket {
        double w, t, f;

        Rocket(double[] arr) {
            this.w = arr[0];
            this.t = arr[1];
            this.f = arr[2];
        }
    }

    private static double[] getArray(int n) throws IOException {
        String[] inputs = br.readLine().split(" ");
        double[] res = new double[n];
        for (int i = 0; i < n; i++) {
            res[i] = Double.parseDouble(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        int K = Integer.parseInt(br.readLine());
        for (int i = 1; i <= K; i++) {
            String[] nm = br.readLine().split(" ");
            int N = Integer.parseInt(nm[0]);
            double M = Double.parseDouble(nm[1]);
            Rocket[] R = new Rocket[N];
            double W = M, V = 0, H = 0;
            for (int j = 0; j < N; j++) {
                R[j] = new Rocket(getArray(3));
                W += R[j].w;
            }
            for (Rocket r: R) {
                double a = r.f / W - 9.81;
                H += V * r.t + 0.5 * a * r.t * r.t;
                V += a * r.t;
                W -= r.w;
            }
            bw.write("Data Set " + i + ":\n");
            bw.write(String.format("%.2f\n", H));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}