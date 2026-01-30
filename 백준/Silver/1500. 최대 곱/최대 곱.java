import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int S = scanner.nextInt();
        int K = scanner.nextInt();
        long ans = 1;
        int a = S;
        int b = K;
        while (b > 0) {
            int n = a / b;
            ans *= n;
            a -= n;
            b--;
        }
        System.out.println(ans);
        scanner.close();
    }
}