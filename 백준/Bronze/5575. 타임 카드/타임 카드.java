import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            int sh = scanner.nextInt();
            int sm = scanner.nextInt();
            int ss = scanner.nextInt();
            int st = sh * 3600 + sm * 60 + ss;

            int eh = scanner.nextInt();
            int em = scanner.nextInt();
            int es = scanner.nextInt();
            int et = eh * 3600 + em * 60 + es;

            int t = et - st;
            int h = t / 3600;
            int m = (t % 3600) / 60;
            int s = (t % 3600) % 60;
            System.out.println(h + " " + m + " " + s);
        }
        scanner.close();
    }
}