import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int MAX = 1000000;
        int[] primes = new int[MAX+1];
        for (int i = 2; i <= MAX; i++) {
            primes[i] = i;
        }
        for (int i = 2; i <= 1000; i++) {
            if (primes[i] == 0) continue;
            for (int j = i*i; j <= MAX; j += i) {
                primes[j] = 0;
            }
        }
        while (true) {
            int N = scanner.nextInt();
            if (N == 0) break;
            boolean flag = false;
            for (int i = 3; i <= N/2; i++) {
                if (primes[i] != 0 && primes[N-i] != 0) {
                    System.out.println(N + " = " + i + " + " + (N-i));
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                System.out.println("Goldbach's conjecture is wrong.");
            }
        }
        scanner.close();
    }
}