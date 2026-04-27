import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int K = sc.nextInt();
        for (int k = 1; k <= K; k++) {
            int L = sc.nextInt();
            int N = sc.nextInt();
            int[] P = new int[N+1];
            for (int i = 1; i <= N; i++) {
                P[i] = sc.nextInt();
            }
            int res = 1;
            while(P[L] != 0) {
                L = P[L];
                res++;
            }
            System.out.println("Data Set " + k + ":");
            System.out.println(res);
            System.out.println();
        }

        sc.close();

    }
}