import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < T; i++) {
            String[] inputs = scanner.nextLine().split(" ");
            double a = Double.parseDouble(inputs[0]);
            String b = inputs[1];
            String c;
            if (b.equals("kg")) {
                a *= 2.2046;
                c = "lb";
            } else if (b.equals("lb")) {
                a *= 0.4536;
                c = "kg";
            } else if (b.equals("l")) {
                a *= 0.2642;
                c = "g";
            } else {
                a *= 3.7854;
                c = "l";
            }
            // a = Math.floor(a * 10000) / 10000;
            System.out.printf("%.4f %s\n", a, c);
        }
        scanner.close();
    }
}