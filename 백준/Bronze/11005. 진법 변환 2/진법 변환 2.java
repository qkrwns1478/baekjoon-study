import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int b = scanner.nextInt();

        char[] nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
        String ans = "";

        while (n != 0) {
            ans = nums[n % b] + ans;
            n /= b;
        }
        System.out.println(ans);
        scanner.close();
    }
}