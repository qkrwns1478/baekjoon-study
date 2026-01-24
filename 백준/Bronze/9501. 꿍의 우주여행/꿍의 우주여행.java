import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int d = scanner.nextInt();
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                int v = scanner.nextInt();
                int f = scanner.nextInt();
                int c = scanner.nextInt();
                if (v * ((double) f / c) >= d) cnt++;
            }
            System.out.println(cnt);
        }
        scanner.close();
    }
}