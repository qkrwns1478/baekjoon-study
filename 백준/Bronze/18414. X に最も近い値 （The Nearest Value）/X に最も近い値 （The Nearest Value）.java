import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int L = scanner.nextInt();
        int R = scanner.nextInt();
        if (L <= X && X <= R) System.out.println(X);
        else if (X < L) System.out.println(L);
        else System.out.println(R);
        scanner.close();
    }
}