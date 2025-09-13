import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Gnomes:");
        for (int i = 0; i < n; i++) {
            String[] inputs = scanner.nextLine().split(" ");
            int a = Integer.parseInt(inputs[0]);
            int b = Integer.parseInt(inputs[1]);
            int c = Integer.parseInt(inputs[2]);
            if ((a >= b && b >= c) || (a <= b && b <= c)) {
                System.out.println("Ordered");
            } else {
                System.out.println("Unordered");
            }
        }
        scanner.close();
    }
}