import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int answer = (int) Math.pow(Math.pow(2, n)+1, 2);
        System.out.println(answer);
        scanner.close();
    }
}