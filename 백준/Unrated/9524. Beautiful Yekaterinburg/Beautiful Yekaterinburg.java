import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int D = scanner.nextInt();
        int[] A = {0, 1, 7, 2, 3};
        System.out.println(A[D]);
        scanner.close();
    }
}
