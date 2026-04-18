import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        String input = br.readLine();
        StringBuilder ans = new StringBuilder(input);
        for (int i = 0; i < N; i++) {
            char c = ans.charAt(i);
            if (Character.isAlphabetic(c))
                ans.setCharAt(N-i-1, c);
        }
        for (int i = 0; i < N; i++) {
            if (ans.charAt(i) == '?') ans.setCharAt(i, 'a');
        }
        bw.write(ans.toString());

        bw.flush();
        bw.close();
        br.close();
    }
}