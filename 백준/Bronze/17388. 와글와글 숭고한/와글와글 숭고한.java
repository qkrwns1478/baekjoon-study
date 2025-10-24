import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
        int k = scanner.nextInt();
        int h = scanner.nextInt();
        if (s + k + h >= 100) System.out.println("OK");
        else {
            if (min(s, k, h) == s) {
                System.out.println("Soongsil");
            } else if (min(s, k, h) == k) {
                System.out.println("Korea");
            } else {
                System.out.println("Hanyang");
            }
        }
        scanner.close();
    }

    private static int min(int a, int b, int c) {
        if (a < b && a < c) return a;
        else if (b < a && b < c) return b;
        else return c;
    }
}