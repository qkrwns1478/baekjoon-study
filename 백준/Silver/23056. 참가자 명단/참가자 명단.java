import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        ArrayList<ArrayList<String>> A = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            A.add(new ArrayList<>());
        }

        while (true) {
            inputs = br.readLine().split(" ");
            int c = Integer.parseInt(inputs[0]);
            String name = inputs[1];
            if (c == 0 && name.equals("0")) break;
            if (A.get(c).size() < M) A.get(c).add(name);
        }

        StringBuilder teamBlue = new StringBuilder();
        StringBuilder teamWhite = new StringBuilder();

        for (int i = 1; i < N+1; i++) {
            if (A.get(i).isEmpty()) continue;
            A.get(i).sort((a, b) -> {
                if (a.length() != b.length()) return a.length() - b.length();
                return a.compareTo(b);
            });
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < A.get(i).size(); j++) {
                sb.append(String.valueOf(i)).append(" ").append(A.get(i).get(j)).append("\n");
            }
            (i % 2 == 1 ? teamBlue : teamWhite).append(sb);
        }

        bw.write(teamBlue.toString());
        bw.write(teamWhite.toString());

        bw.flush();
        bw.close();
        br.close();
    }
}