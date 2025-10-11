import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            int n = scanner.nextInt();
            if (n % 2 == 1) {
                arr.add(n);
            }
        }
        if (arr.isEmpty()) {
            System.out.println(-1);
        } else {
            int sum = 0;
            for (int i: arr) {
                sum += i;
            }
            System.out.println(sum);
            System.out.println(Collections.min(arr));
        }
        scanner.close();
    }
}