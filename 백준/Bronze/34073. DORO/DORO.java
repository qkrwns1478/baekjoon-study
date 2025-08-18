import java.util.Scanner;
import java.util.StringJoiner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();

        String[] s = scanner.nextLine().split(" ");
        for (int i = 0; i < n; i++) {
            if (i < s.length) {
                s[i] += "DORO";
            }
        }

        StringJoiner sj = new StringJoiner(" ");
        for (String str : s) {
            sj.add(str);
        }
        System.out.println(sj.toString());
    }
}