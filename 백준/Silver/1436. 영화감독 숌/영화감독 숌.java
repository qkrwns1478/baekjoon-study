import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int a = 666;
        int c = 1;
        while (c < n) {
            a += 1;
            if (String.valueOf(a).contains("666")) {
                c += 1;
            }
        }
        System.out.println(a);
        scanner.close();
    }
}