import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        n %= 8;
        int result;
        if (n > 5 || n == 0) {
            result = (10 - n) % 8;
        } else {
            result = n;
        }
        System.out.println(result);
        scanner.close();
    }
}