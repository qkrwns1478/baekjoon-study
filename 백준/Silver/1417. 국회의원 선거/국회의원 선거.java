import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        if (N == 1) {
            System.out.println(0);
        } else {
            int[] arr = new int[N-1];
            int dasom = scanner.nextInt();
            for (int i = 0; i < N-1; i++) {
                arr[i] = scanner.nextInt();
            }
            Arrays.sort(arr);
            int answer = 0;
            while (arr[N-2] >= dasom) {
                answer++;
                dasom++;
                arr[N-2]--;
                Arrays.sort(arr);
            }
            System.out.println(answer);
        }
        scanner.close();
    }
}