import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int E = Integer.parseInt(br.readLine());
        ArrayList<Set<Integer>> A = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            A.add(new HashSet<>());
        }
        int cnt = 0;
        for (int i = 0; i < E; i++) {
            String[] inputs = br.readLine().split(" ");
            int K = Integer.parseInt(inputs[0]);
            HashSet<Integer> people = new HashSet<>();
            for (int j = 1; j <= K; j++) {
                people.add(Integer.parseInt(inputs[j]));
            }
            if (people.contains(1)) {
                cnt++;
                for (int p: people) {
                    A.get(p).add(cnt);
                }
            } else {
                HashSet<Integer> tmp = new HashSet<>();
                for (int p: people) {
                    tmp.addAll(A.get(p));
                }
                for (int p: people) {
                    A.remove(p);
                    A.add(p, new HashSet<>(tmp));
                }
            }
        }
        for (int i = 1; i <= N; i++) {
            if (A.get(i).size() == cnt) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}