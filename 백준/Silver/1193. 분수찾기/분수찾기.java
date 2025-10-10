import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int i = 0;
        while (i < x) {
            x -= i;
            i++;
        }
        int a, b;
        if (i % 2 == 1) {
            a = i - x + 1;
            b = x;
        } else {
            a = x;
            b = i - x + 1;
        }
        System.out.println(a + "/" + b);
        scanner.close();
    }
}