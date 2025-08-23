import java.util.Scanner;

public class Main {
    private static final int INF = 1000000000;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] inputNums = input.split(" ");
        int c = Integer.parseInt(inputNums[0]);
        int n = Integer.parseInt(inputNums[1]);

        int arr[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            String tmp = scanner.nextLine();
            String[] tmpNums = tmp.split(" ");
            arr[i][0] = Integer.parseInt(tmpNums[0]);
            arr[i][1] = Integer.parseInt(tmpNums[1]);
        }

        int[] dp = new int[c+101];
        for (int i = 1; i <= c+100; i++) {
            dp[i] = INF;
        }

        for (int[] city: arr) {
            int cost = city[0];
            int nums = city[1];
            for (int i = nums; i <= c+100; i++) {
                dp[i] = Math.min(dp[i], dp[i-nums] + cost);
            }
        }

        int minValue = INF;
        for (int i = 0; i <= 100; i++) {
            minValue = Math.min(minValue, dp[c+i]);
        }
        System.out.println(minValue);

        scanner.close();
    }
}