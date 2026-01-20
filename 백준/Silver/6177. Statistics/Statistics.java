import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        double[] arr = new double[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextDouble();
        }
        Arrays.sort(arr);
        System.out.printf("%.6f\n", Arrays.stream(arr).sum() / N);

        double median = 0;
        if (N % 2 == 0) {
            if (N > 2) {
                median = (arr[N/2-1] + arr[N/2]) / 2;
            } else {
                median = (arr[0] + arr[1]) / 2;
            }
        } else {
            median = arr[N/2];
        }
        System.out.printf("%.6f\n", median);
        scanner.close();
    }
}