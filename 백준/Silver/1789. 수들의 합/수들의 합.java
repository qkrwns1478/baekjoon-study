import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long N = scanner.nextLong();
        long i = 0;
        long cnt = 0;
        while (true) {
            if (N > i) {
                i++;
                N -= i;
                cnt++;
            } else {
                System.out.println(cnt);
                break;
            }
        }
        scanner.close();
    }
}