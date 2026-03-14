import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        for (int i = X; i <=Y; i++) {
            int j = i - X;
            if (j % 3 == 0 && j % 4 == 0 && j % 5 == 0) {
                System.out.println("All positions change in year " + i);
            }
        }
        scanner.close();
    }
}