import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] nums = scanner.nextLine().split(" ");
        int n = Integer.parseInt(nums[0]);
        // int m = Integer.parseInt(nums[0]);
        for (int i = 0; i < n; i++) {
            String s = scanner.nextLine();
            StringBuilder sb = new StringBuilder(s);
            System.out.println(sb.reverse());
        }
        scanner.close();
    }
}