import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            arr.add(scanner.nextInt());
        }
        int ans = 0;
        for (int i = 0; i < arr.size(); i++) {
            int cur = arr.get(i);
            int cnt = 0;
            for (int j = 0; j < arr.size(); j++) {
                if (arr.get(j) == cur)
                    cnt++;
            }
            if (cnt > ans)
                ans = cnt;
        }
        System.out.println(ans);
        scanner.close();
    }
}