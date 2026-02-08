import java.util.Scanner;

public class Main {
    static final int MAX = 10000;
    static final int MIN = -10000;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int max_X = MIN; int min_X = MAX;
        int max_Y = MIN; int min_Y = MAX;
        for (int i = 0; i < N; i++) {
            int X = scanner.nextInt();
            int Y = scanner.nextInt();
            if (max_X < X) max_X = X;
            if (min_X > X) min_X = X;
            if (max_Y < Y) max_Y = Y;
            if (min_Y > Y) min_Y = Y;
        }
        System.out.println((max_X - min_X) * (max_Y - min_Y));
        scanner.close();
    }
}
