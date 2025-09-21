import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] scores1 = new int[4];
        for (int i = 0; i < 4; i++) {
            scores1[i] = scanner.nextInt();
        }
        Arrays.sort(scores1);
        int[] scores2 = new int[2];
        for (int i = 0; i < 2; i++) {
            scores2[i] = scanner.nextInt();
        }
        Arrays.sort(scores2);
        System.out.println(scores1[3]+ scores1[2]+ scores1[1]+scores2[1]);
        scanner.close();
    }
}