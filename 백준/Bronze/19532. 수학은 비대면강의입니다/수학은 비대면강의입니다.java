import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);
        int d = Integer.parseInt(input[3]);
        int e = Integer.parseInt(input[4]);
        int f = Integer.parseInt(input[5]);

        int[] ans = getXY(a, b, c, d, e, f);
        System.out.println(ans[0] + " " + ans[1]);
        scanner.close();
    }

    private static int[] getXY(int a, int b, int c, int d, int e, int f) {
        int[] res = new int[2];
        for (int i = -999; i < 1000; i++) {
            for (int j = -999; j < 1000; j++) {
                if (a*i + b*j == c && d*i + e*j == f) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }
        return res;
    }
}