import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
        int m = scanner.nextInt();
        int l = scanner.nextInt();
        int sum = s + m * 2 + l * 3;
        if (sum >= 10) {
            System.out.println("happy");
        } else {
            System.out.println("sad");
        }
        scanner.close();
    }
}