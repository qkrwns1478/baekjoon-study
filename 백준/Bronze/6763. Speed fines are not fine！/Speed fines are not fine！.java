import java.util.Scanner;

public class Main {
    private final static byte[] arrC = {67, 111, 110, 103, 114, 97, 116, 117, 108, 97, 116, 105, 111, 110, 115, 44, 32, 121, 111, 117, 32, 97, 114, 101, 32, 119, 105, 116, 104, 105, 110, 32, 116, 104, 101, 32, 115, 112, 101, 101, 100, 32, 108, 105, 109, 105, 116, 33};
    private final static byte[] arrY = {89, 111, 117, 32, 97, 114, 101, 32, 115, 112, 101, 101, 100, 105, 110, 103, 32, 97, 110, 100, 32, 121, 111, 117, 114, 32, 102, 105, 110, 101, 32, 105, 115, 32, 36, 37, 100, 46};

    private static int getFine(int speed) {
        if (speed >= 1 && speed <= 20) {
            return 100;
        } else if (speed >= 21 && speed <= 30) {
            return 270;
        } else {
            return 500;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        if (A < B) {
            int F = getFine(B - A);
            System.out.printf(new String(arrY), F);
        } else {
            System.out.println(new String(arrC));
        }
        scanner.close();
    }
}