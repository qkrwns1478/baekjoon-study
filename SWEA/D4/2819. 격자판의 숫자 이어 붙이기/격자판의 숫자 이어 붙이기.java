import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.HashSet;

public class Solution {
	private static Scanner sc = new Scanner(System.in);;
	private static final int N = 4;
	private static final int[] dx = {1, 0, -1, 0};
	private static final int[] dy = {0, 1, 0, -1};
	
	public static void main(String[] args) {
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			System.out.println("#" + tc + " " + solution());
		}
		
		sc.close();
	}
	
	private static Queue<Integer[]> queue;
	private static HashSet<Integer> res;
	private static int[][] arr;
	
	private static int solution() {
		arr = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		res = new HashSet<>();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				bfs(i, j);
			}
		}
		
		return res.size();
	}
	
	private static void bfs(int sx, int sy) {
		queue = new LinkedList<>();
		queue.add(new Integer[] {arr[sx][sy], sx, sy, 1});
		
		while(!queue.isEmpty()) {
			Integer[] cur = queue.poll();
			int num = cur[0], x = cur[1], y = cur[2], cnt = cur[3];
			
			if (cnt == 7) {
				res.add(num);
				continue;
			}
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (isValid(nx) && isValid(ny)) {
					int nextNum = num * 10 + arr[nx][ny];
					queue.add(new Integer[] {nextNum, nx, ny, cnt+1});
				}
			}
		}
	}
	
	private static boolean isValid(int n) {
		return 0 <= n && n < N;
	}
}
