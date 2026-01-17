import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long M = scanner.nextLong();
        int K = scanner.nextInt();
        long C = scanner.nextLong();
        System.out.println(M * C);
        scanner.close();
    }
}