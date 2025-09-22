import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.nextLine();
        HashSet<String> s = new HashSet<>();
        for (int i = 0; i < S.length(); i++) {
            for (int j = i + 1; j <= S.length(); j++) {
                s.add(S.substring(i, j));
            }
        }
        System.out.println(s.size());
        scanner.close();
    }
}