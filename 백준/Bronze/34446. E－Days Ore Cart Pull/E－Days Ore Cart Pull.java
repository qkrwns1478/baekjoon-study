import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static class Calculator {
        int a, b;

        Calculator(int a, int b) {
            this.a = a;
            this.b = b;
        }

        int multiply() {
            return this.a * this.b;
        }
    }

    public static void main(String[] args) throws IOException {

        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int T = Integer.parseInt(br.readLine());
        int ans = new Calculator(M, 2).multiply()
                + new Calculator(N, 0).multiply()
                + new Calculator(T, 0).multiply();
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}