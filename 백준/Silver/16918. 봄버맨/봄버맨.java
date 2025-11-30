import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static Queue<Integer[]> queue = new LinkedList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        int C = scanner.nextInt();
        int N = scanner.nextInt();
        scanner.nextLine();

        int[][] arr = new int[R][C];
        for (int i = 0; i < R; i++) {
            String s = scanner.nextLine();
            for (int j = 0; j < C; j++) {
                if (s.charAt(j) == 'O') arr[i][j] = 1;
                else arr[i][j] = -1;
            }
        }

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        int time = 1;

        while (time < N) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    arr[i][j]++;
                    if (arr[i][j] == 3)
                        queue.add(new Integer[]{i, j});
                }
            }
            while (!queue.isEmpty()) {
                Integer[] cur = queue.remove();
                int x = cur[0];
                int y = cur[1];
                arr[x][y] = -1;
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (0 <= nx && nx < R && 0 <= ny && ny < C)
                        arr[nx][ny] = -1;
                }
            }
            time++;
        }
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                System.out.print(arr[i][j] != -1 ? 'O' : '.');
            }
            System.out.println();
        }
        scanner.close();
    }
}