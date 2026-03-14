import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] nums = new int[3];
        for (int i = 0; i < 3; i++) {
            nums[i] = scanner.nextInt();
        }
        Arrays.sort(nums);
        int a = nums[0], b = nums[1], c = nums[2];
        if (a*a + b*b == c*c) System.out.println(1);
        else if (a == b && b == c) System.out.println(2);
        else System.out.println(0);
        scanner.close();
    }
}