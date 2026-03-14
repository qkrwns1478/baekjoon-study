import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong();
        long b = scanner.nextLong();
        if (a % 2 ==0 || b % 2 == 0) {
            System.out.println(0);
        } else {
            System.out.println(Math.min(a, b));
        }
    }
}