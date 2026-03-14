import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        int C = scanner.nextInt();
        int N = scanner.nextInt();
        long X = R / N + (R % N > 0 ? 1 : 0);
        long Y = C / N + (C % N > 0 ? 1 : 0);
        System.out.println(X*Y);
        scanner.close();
    }
}