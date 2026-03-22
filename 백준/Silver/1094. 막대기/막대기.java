import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        int len = 64, cur = 64, ans = 1;
        if (X == 64) {
            System.out.println(1);
        } else {
            while (true) {
                cur /= 2;
                len -= cur;
                if (len < X) {
                    ans++;
                    len += cur;
                } else if (len == X) {
                    break;
                }
            }
            System.out.println(ans);
        }
        br.close();
    }
}