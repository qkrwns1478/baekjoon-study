import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] arrStrings = scanner.nextLine().split(" ");
        ArrayList<Integer> arr = new ArrayList<>();
        for (String s : arrStrings) {
            arr.add(Integer.parseInt(s));
        }

        String[] input = scanner.nextLine().split(" ");
        int x = Integer.parseInt(input[0]);
        int y = Integer.parseInt(input[1]);
        int r = Integer.parseInt(input[2]);

        int ans = 0;
        if (arr.contains(x)) {
            ans += arr.indexOf(x) + 1;
        }
        System.out.println(ans);
        scanner.close();
    }
}