import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Solution {
	private static Scanner sc = new Scanner(System.in);
	private static final int[] dx = {1, 0, -1, 0};
	private static final int[] dy = {0, 1, 0, -1};
	
	public static void main(String[] args) {
        final int T = 10;
		for (int i = 1; i <= T; i++) {
			System.out.printf("#%d %d\n", i, solution());
		}
	}
	
	private static int solution() {
		sc.nextLine();
		final int N = 16;
		int[][] arr = new int[N][N];
		int sx = 0, sy = 0, ex = 0, ey = 0;
		
		for (int i = 0; i < N; i++) {
			String tmp = sc.nextLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = tmp.charAt(j) - '0';
				if (arr[i][j] == 2) {
					sx = i; sy = j;
				} else if (arr[i][j] == 3) {
					ex = i; ey = j;
				}
			}
		}
		
		Queue<Integer[]> queue = new LinkedList<>();
		boolean[][] visited = new boolean[N][N];
		queue.add(new Integer[] {sx, sy});
		visited[sx][sy] = true;
		
		while (!queue.isEmpty()) {
			Integer[] cur = queue.poll();
			int x = cur[0], y = cur[1];
			if (x == ex && y == ey)
                return 1;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < N) {
					if (arr[nx][ny] != 1 && !visited[nx][ny]) {
						visited[nx][ny] = true;
						queue.add(new Integer[] {nx, ny});
					}
				}
			}
		}
		
		return 0;
	}
}
