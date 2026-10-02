import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // Please write your code here.
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("add")) {
                int k = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                map.put(k, v);
            } else if (cmd.equals("remove")) {
                int k = Integer.parseInt(st.nextToken());
                map.remove(k);
            } else {
                int k = Integer.parseInt(st.nextToken());
                System.out.println(map.keySet().contains(k) ? map.get(k) : "None");
            }
        }
    }
}