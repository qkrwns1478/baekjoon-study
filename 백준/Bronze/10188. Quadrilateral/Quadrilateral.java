import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            int L = scanner.nextInt();
            int W = scanner.nextInt();
            for (int j = 0; j < W; j++) {
                for (int k = 0; k < L; k++) {
                    System.out.print("X");
                }
                System.out.println();
            }
            if (i != N-1) {
                System.out.println();
            }
        }
        scanner.close();
    }
}