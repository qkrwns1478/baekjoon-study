import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (N == 1)
            System.out.println(3);
        else if (N == 2)
            System.out.println(7);
        else {
            int a = 3;
            int b = 7;
            int c = 17;
            for (int i = 3; i < N+1; i++) {
                c = (a + 2 * b) % 9901;
                a = b;
                b = c;
            }
            System.out.println(c);
        }
        scanner.close();
    }
}