import java.util.Scanner;

public class Main {
    static int n;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();

        for (int row = 0; row < n; row++) {
            drawGb(3, true);
            drawGb(1, false);
            drawGb(1, true);
            System.out.println();
        }

        for (int blockRow = 0; blockRow < 3; blockRow++) {
            for (int row = 0; row < n; row++) {
                drawGb(1, true);
                drawGb(1, false);
                drawGb(1, true);
                drawGb(1, false);
                drawGb(1, true);
                System.out.println();
            }
        }

        for (int row = 0; row < n; row++) {
            drawGb(1, true);
            drawGb(1, false);
            drawGb(3, true);
            System.out.println();
        }

        scanner.close();
    }

    private static void drawGb(int x, boolean flag) {
        int cnt = n * x;
        if (flag) {
            for (int i = 0; i < cnt; i++) {
                System.out.print("@");
            }
        } else {
            for (int i = 0; i < cnt; i++) {
                System.out.print(" ");
            }
        }
    }
}