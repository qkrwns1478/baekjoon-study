import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        HashMap<Character, String> h = new HashMap<Character, String>(N);
        for (int i = 0; i < N; i++) {
            String[] input = scanner.nextLine().split(" ");
            h.put(input[1].charAt(0), input[0]);
        }
        StringBuilder sb = new StringBuilder();
        String str = scanner.nextLine();
        int S = scanner.nextInt();
        int E = scanner.nextInt();
        for(int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            sb.append(h.get(c));
        }
        System.out.println(sb.substring(S-1, E));
        scanner.close();
    }
}