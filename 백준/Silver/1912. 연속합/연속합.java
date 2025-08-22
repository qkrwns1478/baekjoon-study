import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine(); // 버퍼 비우기
        String line = scanner.nextLine();
        String[] strNums = line.split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(strNums[i]);
        }
        int[] dp = new int[n];
        dp[0] = arr[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(arr[i], dp[i-1] + arr[i]);
        }
        System.out.println(getMax(dp));
        scanner.close();
    }

    public static int getMax(int[] dp) {
        int maxValue = -1000;
        for (int j : dp) {
            if (maxValue < j) maxValue = j;
        }
        return maxValue;
    }
}