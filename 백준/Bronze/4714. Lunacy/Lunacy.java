import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            double X = scanner.nextDouble();
            if (X == -1.0) break;
            System.out.printf("Objects weighing %.2f on Earth will weigh %.2f on the moon.\n", X, X * 0.167);
        }
        scanner.close();
    }
}