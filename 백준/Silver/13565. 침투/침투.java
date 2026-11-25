import java.util.*;

public class Main {
	static int M, N;
	static boolean[][] isBlocked;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		M = sc.nextInt();
		N = sc.nextInt();
		sc.nextLine();
		isBlocked = new boolean[M][N];
		for (int i = 0; i < M; i++) {
			String s = sc.nextLine();
			for (int j = 0; j < N; j++) {
				char c = s.charAt(j);
				if (c == '1') isBlocked[i][j] = true;
			}
		}
		
		boolean answer = false;
		for (int i = 0; i < N; i++) {
			if (bfs(0, i)) {
				answer = true;
				break;
			}
		}
		
		System.out.println(answer ? "YES" : "NO");
		sc.close();
	}
	
	static boolean isInRange(int x, int y) {
		return 0 <= x && x < M && 0 <= y && y < N;
	}
	
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	
	static boolean bfs(int sx, int sy) {
		Queue<State> queue = new ArrayDeque<>();
		boolean[][] visited = new boolean[M][N];
		queue.add(new State(sx, sy));
		visited[sx][sy] = true;
		
		while (!queue.isEmpty()) {
			State cur = queue.poll();
			if (cur.x == M-1) return true;
			
			for (int i = 0; i < 4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];
				if (!isInRange(nx, ny) || visited[nx][ny] || isBlocked[nx][ny]) continue;
				visited[nx][ny] = true;
				queue.add(new State(nx, ny));
			}
		}
		
		return false;
	}
	
}

class State {
	int x, y;

	public State(int x, int y) {
		this.x = x;
		this.y = y;
	}
}