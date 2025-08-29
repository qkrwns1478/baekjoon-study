import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = Integer.parseInt(scanner.nextLine());
        for (int t = 0; t < T; t++) {
            scanner.nextLine();
            int n = Integer.parseInt(scanner.nextLine());
            BigInteger total = new BigInteger("0");
            for (int i = 0; i < n; i++) {
                total = total.add(BigInteger.valueOf(Long.parseLong(scanner.nextLine())));
            }
            if (String.valueOf(total.remainder(BigInteger.valueOf(n))).equals("0")) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        scanner.close();
    }
}