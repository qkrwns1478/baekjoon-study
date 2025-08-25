import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] inputNums = input.split(" ");
        int h = Integer.parseInt(inputNums[0]);
        int w = Integer.parseInt(inputNums[1]);

        String line = scanner.nextLine();
        String[] strNums = line.split(" ");
        int[] arr = new int[strNums.length];
        for (int i = 0; i < strNums.length; i++) {
            arr[i] = Integer.parseInt(strNums[i]);
        }

        int answer = 0;
        for (int i = 1; i < w; i++) {
            int maxLeft = 0;
            int maxRight = 0;
            for (int j = 0; j < i; j++) {
                if (maxLeft < arr[j])
                    maxLeft = arr[j];
            }
            for (int j = i+1; j < arr.length; j++) {
                if (maxRight < arr[j])
                    maxRight = arr[j];
            }
            int res = Math.min(maxLeft, maxRight);
            if (arr[i] < res)
                answer += res - arr[i];
        }

        System.out.println(answer);

        scanner.close();
    }
}