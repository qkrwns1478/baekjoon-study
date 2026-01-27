import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        int C = scanner.nextInt();
        int ZR = scanner.nextInt();
        int ZC = scanner.nextInt();
        scanner.nextLine();
        String[] strings = new String[R];
        for (int i = 0; i < R; i++) {
            strings[i] = scanner.nextLine();
        }
        for (int i = 0; i < R; i++) {
            for (int ii = 0; ii < ZR; ii++) {
                for (int j = 0; j < C; j++) {
                    char c = strings[i].charAt(j);
                    for (int jj = 0; jj < ZC; jj++) {
                        System.out.print(c);
                    }
                }
                System.out.println();
            }
        }
        scanner.close();
    }
}