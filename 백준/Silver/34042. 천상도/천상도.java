import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] getArray(int n) throws IOException {
        String[] inputs = br.readLine().split(" ");
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = Integer.parseInt(inputs[i]);
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        int[] arr = getArray(2);
        int N = arr[0], M = arr[1];
        for (int i = 0; i < M; i++) {
            ArrayList<Long> pos = new ArrayList<>();
            ArrayList<Long> neg = new ArrayList<>();
            boolean flagZero = false;
            arr = getArray(N);
            for (int j = 0; j < N; j++) {
                long cur = (long) arr[j];
                if (cur > 0) pos.add(cur);
                else if (cur < 0) neg.add(cur);
                else flagZero = true;
            }
            pos.sort(Collections.reverseOrder());
            Collections.sort(neg);
            long ans;
            if (pos.isEmpty() && neg.isEmpty()) ans = 0;
            else if (pos.isEmpty() && neg.size() == 1) ans = flagZero ? 0 : neg.get(0);
            else {
                ans = 1;
                for (long p: pos) ans *= p;
                int idx = 0;
                while (idx + 1 < neg.size()) {
                    ans *= neg.get(idx) * neg.get(idx + 1);
                    idx += 2;
                }
                if (flagZero) ans = Math.max(ans, 0);
            }
            bw.write(ans + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}