import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < 10000; i++) {
            int x = i, y = i;
            while (y > 0) {
                x += y % 10;
                y /= 10;
            }
            set.add(x);
        }
        for (int i = 1; i <= 10000; i++) {
            if (!set.contains(i)) System.out.println(i);
        }
        scanner.close();
    }
}