import java.util.*;

public class Main {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] cows = new int[N+1];
        int[] arr = new int[N+1];
        for (int i = 0; i <= N; i++) {
            arr[i] = -1;
        }
        for (int i = 0; i < N; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            if (arr[A] == -1) arr[A] = B;
            else if (arr[A] != B) {
                cows[A]++;
                arr[A] = B;
            }
        }

        int ans = 0;
        for (int cow: cows) ans += cow;
        System.out.println(ans);

        sc.close();

    }
}