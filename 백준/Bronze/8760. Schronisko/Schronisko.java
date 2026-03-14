import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int Z = scanner.nextInt();
        for (int z = 0; z < Z; z++) {
            int W = scanner.nextInt();
            int K = scanner.nextInt();
            System.out.println(W*K / 2);
        }
        scanner.close();
    }
}