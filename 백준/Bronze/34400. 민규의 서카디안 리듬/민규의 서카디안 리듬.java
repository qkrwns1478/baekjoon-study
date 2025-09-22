import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int i = 0; i < T; i++) {
            int t = scanner.nextInt();
            if (t % 25 < 17) {
                System.out.println("ONLINE");
            } else {
                System.out.println("OFFLINE");
            }
        }
        scanner.close();
    }
}