import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = scanner.nextInt();
            }
            Arrays.sort(arr);
            int cnt = 0;
            while (arr[n-1] != 0) {
                if (arr[0] != 0) {
                    int m = arr[0];
                    for (int j = 0; j < n; j++) {
                        arr[j] -= m;
                    }
                } else {
                    int nxt = 0;
                    for (int j = 0; j < n; j++) {
                        if (arr[j] != 0) {
                            nxt = arr[j];
                            break;
                        }
                    }
                    for (int j = 0; j < n; j++) {
                        if (arr[j] != 0)
                            break;
                        arr[j] += nxt;
                    }
                }
                cnt++;
            }
            System.out.println(cnt);
        }
        scanner.close();
    }
}