import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < N; i++) {
            String input = scanner.nextLine();
            int cnt = 0;
            for (int j = 0; j < input.length(); j++) {
                char c = input.charAt(j);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
            }
            System.out.println("The number of vowels in " + input + " is " + cnt + ".");
        }
        scanner.close();
    }
}