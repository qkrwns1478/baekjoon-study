import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        if (n == 1) {
            System.out.println("Before");
        } else {
            if (n == 2) {
                if (m == 18) {
                    System.out.println("Special");
                } else if (m < 18) {
                    System.out.println("Before");
                } else {
                    System.out.println("After");
                }
            } else {
                System.out.println("After");
            }
        }
        scanner.close();
    }
}