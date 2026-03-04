import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        scanner.nextLine();
        String S = scanner.nextLine();
        int ans = 0, i = 0, cnt = 0;
        while (i < M-1) {
            if (S.startsWith("IOI", i)) {
                i += 2; cnt++;
                if (cnt == N) {
                    ans++; cnt--;
                }
            } else {
                i++; cnt = 0;
            }
        }
        System.out.println(ans);
        scanner.close();
    }
}