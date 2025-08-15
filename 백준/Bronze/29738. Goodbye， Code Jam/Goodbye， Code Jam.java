import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int x = 1; x <= T; x++) {
            int N = scanner.nextInt();
            if (N <= 25) {
                System.out.println("Case #" + x + ": World Finals");
            } else if (N <= 1000) {
                System.out.println("Case #" + x + ": Round 3");
            } else if (N <= 4500) {
                System.out.println("Case #" + x + ": Round 2");
            } else {
                System.out.println("Case #" + x + ": Round 1");
            }
        }
    }
}