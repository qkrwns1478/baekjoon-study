import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);

        String[] arrStrings = scanner.nextLine().split(" ");
        ArrayList<Integer> arr = new ArrayList<>();
        for (String s : arrStrings) {
            arr.add(Integer.parseInt(s));
        }

        int ans = 0;
        for (int i = 0; i < k; i++) {
            ans += (arr.get(i) + 1) / 2;
        }
        if (ans >= n) System.out.println("YES");
        else System.out.println("NO");
        scanner.close();
    }
}