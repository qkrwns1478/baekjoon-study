import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int a = n / 3;
        int b = n / 5;
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i <= a; i++) {
            for (int j = 0; j <= b; j++) {
                if (3*i + 5*j == n) {
                    ans = Math.min(ans, i + j);
                }
            }
        }
        if (ans == Integer.MAX_VALUE) {
            ans = -1;
        }
        System.out.println(ans);
        scanner.close();
    }
}