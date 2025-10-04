import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = 0;
        ArrayList<String> inputs = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            String s = scanner.nextLine();
            n = Math.max(n, s.length());
            inputs.add(s);
        }

        char[][] arr = new char[5][n];
        for (int i = 0; i < 5; i++) {
            String cur = inputs.get(i);
            for (int j = 0; j < n; j++) {
                if (j < cur.length()) {
                    arr[i][j] = cur.charAt(j);
                } else {
                    arr[i][j] = ' ';
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[j][i] != ' ') {
                    System.out.print(arr[j][i]);
                }
            }
        }

        scanner.close();
    }
}