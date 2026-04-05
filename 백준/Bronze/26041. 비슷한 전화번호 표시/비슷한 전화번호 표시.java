import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        String[] A = br.readLine().split(" ");
        String B = br.readLine();
        int ans = 0;
        for (String a: A) {
            if (a.length() > B.length() && a.startsWith(B)) ans++;
        }
        bw.write(String.valueOf(ans));

        bw.flush();
        bw.close();
        br.close();
    }
}