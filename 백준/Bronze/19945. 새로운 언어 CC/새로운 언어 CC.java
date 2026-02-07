import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (N > 0) {
            String bin = Integer.toBinaryString(N);
            System.out.println(bin.length());
        } else if (N == 0)
            System.out.println(1);
        else
            System.out.println(32);
        scanner.close();
    }
}
