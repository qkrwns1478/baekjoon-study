import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String s = scanner.nextLine();
            if (s.equals("0+0=0")) {
                System.out.println("True");
                break;
            }
            String[] parts = s.split("\\+");
            String a = parts[0];
            String[] parts2 = parts[1].split("=");
            String b = parts2[0];
            String c = parts2[1];

            int ia = Integer.parseInt(new StringBuilder(a).reverse().toString());
            int ib = Integer.parseInt(new StringBuilder(b).reverse().toString());
            int ic = Integer.parseInt(new StringBuilder(c).reverse().toString());

            System.out.println(ia + ib == ic ? "True" : "False");
        }
        scanner.close();
    }
}