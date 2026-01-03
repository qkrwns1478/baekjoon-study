import java.util.Scanner;
import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int ans = (int) sqrt(N);
        System.out.println("The largest square has side length " + ans + ".");
        scanner.close();
    }
}