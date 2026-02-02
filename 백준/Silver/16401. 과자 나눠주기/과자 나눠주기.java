import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int M = scanner.nextInt();
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        Arrays.sort(arr);
        int left = 1;
        int right = arr[N-1];
        int answer = 0;
        while (left <= right) {
            int cnt = 0;
            int mid = (left + right) / 2;
            for (int i = 0; i < N; i++) {
                cnt += arr[i] / mid;
            }
            if (cnt >= M) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(answer);
        scanner.close();
    }
}