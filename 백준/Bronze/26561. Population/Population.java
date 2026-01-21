import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            int P = scanner.nextInt();
            int T = scanner.nextInt();
            System.out.println(P + T / 4 - T / 7);
        }
        scanner.close();
    }
}