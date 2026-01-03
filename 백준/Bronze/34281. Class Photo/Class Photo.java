import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long w = scanner.nextLong();
        long l = scanner.nextLong();
        System.out.println(w * l);
        scanner.close();
    }
}