import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] nums = scanner.nextLine().split(" ");
        int n = Integer.parseInt(nums[0]);
        int m = Integer.parseInt(nums[1]);
        HashSet<String> s = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String input = scanner.nextLine();
            s.add(input);
        }
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            String t = scanner.nextLine();
            if (s.contains(t)) {
                cnt++;
            }
        }
        System.out.println(cnt);
        scanner.close();
    }
}