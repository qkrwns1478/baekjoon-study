import java.util.Scanner;

public class Main {
    static int Y = 0;
    static int K = 0;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < N; i++) {
            String s = scanner.nextLine();
            if (s.equals("yonsei")) Y = i;
            else if (s.equals("korea")) K = i;
        }
        String res = Y < K ? "Won!" : "Lost...";
        System.out.println("Yonsei " + res);
        scanner.close();
    }
}