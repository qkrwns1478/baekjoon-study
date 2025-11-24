import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        String A = input[0];
        String B = input[1];
        long answer = 0;
        for (int i = 0; i < A.length(); i++) {
            for (int j = 0; j < B.length(); j++) {
                long a = A.charAt(i) - '0';
                long b = B.charAt(j) - '0';
                answer += a * b;
            }
        }
        System.out.println(answer);
        scanner.close();
    }
}