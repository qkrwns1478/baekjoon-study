import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int V = scanner.nextInt();
            int E = scanner.nextInt();
            System.out.println(2-V+E);
        }
        scanner.close();
    }
}