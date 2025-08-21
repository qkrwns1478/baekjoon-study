import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine(); 

        String[] cStr = scanner.nextLine().split(" ");
        double[] c = new double[n];
        for (int i = 0; i < n; i++) {
            c[i] = Double.parseDouble(cStr[i]);
        }

        double total = 0;
        for (int i = 0; i < n; i++) {
            total += Math.pow(c[i], 3);
        }
        System.out.println(Math.pow(total, 1.0/3.0));
    }
}