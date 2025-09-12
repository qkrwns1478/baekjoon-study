import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputs = scanner.nextLine().split(" ");
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = Integer.parseInt(inputs[i]);
        }
        int[] answer = {1, 2, 3, 4, 5};
        while (true) {
            for (int i = 0; i < 4; i++) {
                if (arr[i] > arr[i+1]) {
                    int tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
                    for (int j = 0; j < 5; j++) {
                        System.out.print(arr[j] + (j == 4 ? "" : " "));
                    }
                    System.out.println();
                }
            }
            if (Arrays.equals(arr, answer))
                break;
        }
        scanner.close();
    }
}