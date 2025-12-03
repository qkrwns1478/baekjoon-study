import java.util.HashMap;
import java.util.Scanner;

public class Main {
    private static final boolean[][] arr = new boolean[5][5];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<Integer, Integer[]> hashMap = new HashMap<>();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                int k = scanner.nextInt();
                hashMap.put(k, new Integer[]{i, j});
            }
        }

        for (int i = 1; i <= 25; i++) {
            int k = scanner.nextInt();
            Integer[] cur = hashMap.get(k);
            int x = cur[0];
            int y = cur[1];
            arr[x][y] = true;
            if (check()) {
                System.out.println(i);
                break;
            }
        }
        scanner.close();
    }

    private static boolean check() {
        int score = 0;
        for (int i = 0; i < 5; i++) {
            if (arr[i][0] == arr[i][1] && arr[i][1] == arr[i][2] &&
                    arr[i][2] == arr[i][3] && arr[i][3] == arr[i][4] && arr[i][4] == true) {
                score++;
            }
            if (arr[0][i] == arr[1][i] && arr[1][i] == arr[2][i] &&
                    arr[2][i] == arr[3][i] && arr[3][i] == arr[4][i] && arr[4][i] == true) {
                score++;
            }
        }
        if (arr[0][0] == arr[1][1] && arr[1][1] == arr[2][2] && arr[2][2] == arr[3][3] &&
                    arr[3][3] == arr[4][4] && arr[4][4] == true) {
            score++;
        }
        if (arr[4][0] == arr[3][1] && arr[3][1] == arr[2][2] && arr[2][2] == arr[1][3] &&
                arr[1][3] == arr[0][4] && arr[0][4] == true) {
            score++;
        }
        return score >= 3;
    }
}
