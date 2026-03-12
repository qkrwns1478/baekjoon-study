import java.util.*;

public class Main {
    private static int calc(int a, String o, int b) {
        if (o.equals("+")) return a + b;
        else if (o.equals("-")) return a - b;
        else if (o.equals("*")) return a * b;
        else if (o.equals("/")) {
            if (a > 0 && b > 0) return a / b;
            else if (a < 0 && b < 0) return a / b;
            else if (a < 0) return -(-a / b);
            else return -(a / -b);
        }
        else return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputs = scanner.nextLine().split(" ");
        int K1 = Integer.parseInt(inputs[0]);
        String O1 = inputs[1];
        int K2 = Integer.parseInt(inputs[2]);
        String O2 = inputs[3];
        int K3 = Integer.parseInt(inputs[4]);
        int A1 = calc(calc(K1, O1, K2), O2, K3);
        int A2 = calc(K1, O1, calc(K2, O2, K3));
        System.out.println(Math.min(A1, A2));
        System.out.println(Math.max(A1, A2));
        scanner.close();
    }
}