import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        if (N % 2 == 0 || M % 2 == 0) System.out.println("A");
        else System.out.println("B");
        scanner.close();
    }
}