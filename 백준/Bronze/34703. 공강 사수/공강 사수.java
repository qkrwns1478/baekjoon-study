import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int mask = 0;
        while (N-- > 0) {
            mask |= 1 << (sc.nextInt() - 1);
        }
        System.out.println(mask != 31 ? "YES" : "NO");

    }
}