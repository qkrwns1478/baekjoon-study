import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        String S = scanner.nextLine();
        for (int i = 0; i < N-1; i++) {
            if (S.charAt(i+1) == 'J') {
                System.out.println(S.charAt(i));
            }
        }
        scanner.close();
    }
}