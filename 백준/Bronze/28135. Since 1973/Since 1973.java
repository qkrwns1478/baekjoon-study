import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long N = scanner.nextLong();
        long ans = 0;
        for (long i = 1; i <= N; i++) {
            String numStr = String.valueOf(i-1);
            if (numStr.contains("50")) ans += 2;
            else ans += 1;
        }
        System.out.println(ans);
        scanner.close();
    }
}