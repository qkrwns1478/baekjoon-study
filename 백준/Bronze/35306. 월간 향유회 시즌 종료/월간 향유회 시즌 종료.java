import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int K = Integer.parseInt(inputs[1]);
        int[] MAX = new int[K];
        ArrayList<ArrayList<Integer>> LIST = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            LIST.add(new ArrayList<>());
        }

        for (int i = 0; i < N; i++) {
            inputs = br.readLine().split(" ");
            for (int j = 0; j < K; j++) {
                int t = Integer.parseInt(inputs[j]);
                if (t > MAX[j]) {
                    MAX[j] = t;
                    LIST.get(j).clear();
                    LIST.get(j).add(i);
                } else if (t == MAX[j]) {
                    LIST.get(j).add(i);
                }
            }
        }

        HashSet<Integer> candidate = new HashSet<>();
        for (int i = 0; i < K; i++) {
            if (LIST.get(i).size() == 1) {
                candidate.add(LIST.get(i).get(0));
            }
        }
        System.out.println(candidate.size());
        br.close();
    }
}