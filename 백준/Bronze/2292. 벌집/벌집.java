import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int hex = 1;
        int cnt = 1;
        while (n > hex) {
            hex += 6 * cnt;
            cnt++;
        }
        System.out.println(cnt);
        scanner.close();
    }
}