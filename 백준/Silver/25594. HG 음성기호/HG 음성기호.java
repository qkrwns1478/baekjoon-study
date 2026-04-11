import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static final String[] HG = {"aespa", "baekjoon", "cau", "debug",
            "edge", "firefox", "golang", "haegang", "iu", "java", "kotlin",
            "lol", "mips", "null", "os", "python", "query", "roka", "solvedac",
            "tod", "unix", "virus", "whale", "xcode", "yahoo", "zebra"};

    private static final StringBuilder sb = new StringBuilder();

    private static int index(char c) {
        return (int) c - 97;
    }

    public static void main(String[] args) throws IOException {
        String S = br.readLine();
        StringBuilder ans = new StringBuilder();
        boolean flag = true;

        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            sb.append(c);
            int idx = index(sb.charAt(0));
            if (sb.length() == HG[idx].length()) {
                if (sb.toString().equals(HG[idx])) {
                    ans.append(sb.charAt(0));
                    sb.delete(0, sb.length());
                } else {
                    flag = false;
                    break;
                }
            }
        }

        if (!sb.isEmpty()) flag = false;
        bw.write(flag ? "It's HG!\n" + ans : "ERROR!");

        bw.flush();
        bw.close();
        br.close();
    }
}