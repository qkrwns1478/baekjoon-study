import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < t; i++) {
            String[] intStr = scanner.nextLine().split(" ");
            int g = Integer.parseInt(intStr[0]);
            int c = Integer.parseInt(intStr[1]);
            int e = Integer.parseInt(intStr[2]);
            if (c >= e) {
                System.out.println(0);
            } else {
                int k = 2 * g - 1;
                System.out.println((e - c) * k);
            }
        }
    }
}