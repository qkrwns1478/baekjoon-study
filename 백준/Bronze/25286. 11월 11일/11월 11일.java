import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < T; i++) {
            String[] input = scanner.nextLine().split(" ");
            int y = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[1]);
            int d = 0;
            int[] days = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            if (m == 1) {
                y--;
                m = 12;
                d = 31;
            } else if (m == 3) {
                m--;
                if ((y % 100 != 0 && y % 4 == 0) || y % 400 == 0) {
                    d = 29;
                } else {
                    d = 28;
                }
            } else {
                m--;
                d = days[m];
            }
            System.out.printf("%d %d %d\n", y, m, d);
        }
        scanner.close();
    }
}