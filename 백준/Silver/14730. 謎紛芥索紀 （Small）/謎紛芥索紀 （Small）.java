import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int answer = 0;
        for (int i = 0; i < N; i++) {
            int C = scanner.nextInt();
            int K = scanner.nextInt();
            answer += C * K;
        }
        System.out.println(answer);
        scanner.close();
    }
}