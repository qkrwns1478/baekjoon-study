import java.util.*;
import java.io.*;

public class Main {
    static LinkedList<Character> ll = new LinkedList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        for (int i = 0; i < str.length(); i++) {
            ll.add(str.charAt(i));
        }

        ListIterator<Character> li = ll.listIterator(ll.size());
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            String[] inputs= br.readLine().split(" ");
            char cmd = inputs[0].charAt(0);
            if (cmd == 'L' && li.hasPrevious()) {
                li.previous();
            } else if (cmd == 'D' && li.hasNext()) {
                li.next();
            } else if (cmd == 'B' && li.hasPrevious()) {
                li.previous();
                li.remove();
            } else if (cmd == 'P') {
                li.add(inputs[1].charAt(0));
            }
        }

        for (char c: ll) {
            bw.write(c);
        }

        bw.flush();
        bw.close();
        br.close();
    }
}