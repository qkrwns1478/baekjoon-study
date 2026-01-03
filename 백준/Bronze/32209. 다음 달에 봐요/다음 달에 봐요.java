import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int Q = scanner.nextInt();
        int questions = 0;
        boolean flag = true;
        for (int i = 0; i < Q; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            if (x == 1) questions += y;
            else questions -= y;
            if (questions < 0) {
                flag = false;
                break;
            }
        }
        System.out.println(flag ? "See you next month" : "Adios");
        scanner.close();
    }
}