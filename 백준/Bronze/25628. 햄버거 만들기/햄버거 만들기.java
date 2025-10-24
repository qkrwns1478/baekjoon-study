import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int cnt = Math.min(a/2, b);
        System.out.println(cnt);
        scanner.close();
    }
}