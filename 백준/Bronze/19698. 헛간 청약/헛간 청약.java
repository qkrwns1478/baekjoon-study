import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int W = scanner.nextInt();
        int H = scanner.nextInt();
        int L = scanner.nextInt();
        System.out.println(Math.min(N, (W/L)*(H/L)));
        scanner.close();
    }
}