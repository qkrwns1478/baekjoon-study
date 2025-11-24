import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        BigInteger a = new BigInteger(input[0], 2);
        BigInteger b = new BigInteger(input[1], 2);
        BigInteger c = a.add(b);
        System.out.println(c.toString(2));
        scanner.close();
    }
}