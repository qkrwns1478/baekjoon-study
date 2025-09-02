import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < t; i++) {
            String[] input = scanner.nextLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            // int c = (int) Math.pow(a, b) % 10;
            int c = 1;
            for (int j = 0; j < b; j++)
                c = (c * a) % 10;
            if (c == 0)
                c += 10;
            System.out.println(c);
        }
        scanner.close();
    }
}