import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int k = scanner.nextInt();
        int w = scanner.nextInt();
        int m = scanner.nextInt();
        double x = (double) (w - k) / m;
        System.out.println((int) Math.ceil(x));
        scanner.close();
    }
}