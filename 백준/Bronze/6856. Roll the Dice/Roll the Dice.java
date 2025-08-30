import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        int cnt = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (i + j == 10) {
                    cnt++;
                }
            }
        }
        if (cnt == 1)
            System.out.println("There is 1 way to get the sum 10.");
        else
            System.out.println("There are " + cnt + " ways to get the sum 10.");
        scanner.close();
    }
}