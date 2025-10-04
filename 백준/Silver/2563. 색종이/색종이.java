import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] arr = new int[100][100];

        for (int k = 0; k < n; k++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            for (int i = x; i < x + 10; i++) {
                for (int j = y; j < y + 10; j++) {
                    arr[i][j] = 1;
                }
            }
        }

        int cnt = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (arr[i][j] == 1) {
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
        scanner.close();
    }
}