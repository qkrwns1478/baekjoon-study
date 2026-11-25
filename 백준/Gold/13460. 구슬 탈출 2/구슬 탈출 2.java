import java.io.*;
import java.util.*;

class State {
	int bx, by, rx, ry, cnt;

	public State(int bx, int by, int rx, int ry, int cnt) {
		this.bx = bx;
		this.by = by;
		this.rx = rx;
		this.ry = ry;
		this.cnt = cnt;
	}
	
	public State(Marble blue, Marble red, int cnt) {
		this.bx = blue.x;
		this.by = blue.y;
		this.rx = red.x;
		this.ry = red.y;
		this.cnt = cnt;
	}
}

class MoveDTO {
	boolean isValid;
	State state;
	
	public MoveDTO(boolean isValid, State state) {
		this.isValid = isValid;
		this.state = state;
	}
}

class Marble {
	int x, y;
	
	public Marble(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static int N, M;
	static int sbx, sby, srx, sry, hx, hy;
	static boolean[][] isBlocked;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		isBlocked = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			String s = br.readLine();
			for (int j = 0; j < M; j++) {
				char c = s.charAt(j);
				if (c == '.') continue;
				else if (c == '#') isBlocked[i][j] = true;
				else if (c == 'B') { sbx = i; sby = j; }
				else if (c == 'R') { srx = i; sry = j; }
				else if (c == 'O') { hx = i; hy = j; }
			}
		}
		
		System.out.println(bfs());
		br.close();
	}
	
	static boolean isInRange(int x, int y) {
		return 0 <= x && x < N && 0 <= y && y < M;
	}
	
	static boolean isInHole(Marble m) {
		return m.x == hx && m.y == hy;
	}
	
	static String getStringCoord(State s) {
		return String.format("%d,%d,%d,%d", s.bx, s.by, s.rx, s.ry);
	}
	
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	
	static void move(Marble m, int d, int ax, int ay) {
		if (isInHole(m)) return;
		
		int nx, ny;
		while (true) {
			nx = m.x + dx[d];
			ny = m.y + dy[d];
			if (isBlocked[nx][ny]) break;
			if (nx == ax && ny == ay) break;
			m.x = nx;
			m.y = ny;
			if (isInHole(m)) break;
		}
	}
	
	static MoveDTO move(State cur, int d) {
		Marble blue = new Marble(cur.bx, cur.by);
		Marble red = new Marble(cur.rx, cur.ry);
		
		// 먼저 움직일 구슬 정하기
		Marble first, second;
		if (d == 0) {
			first = blue.x >= red.x ? blue : red;
			second = blue.x >= red.x ? red : blue;
		} else if (d == 1) {
			first = blue.y >= red.y ? blue : red;
			second = blue.y >= red.y ? red : blue;
		} else if (d == 2) {
			first = blue.x >= red.x ? red : blue;
			second = blue.x >= red.x ? blue : red;
		} else {
			first = blue.y >= red.y ? red : blue;
			second = blue.y >= red.y ? blue : red;
		}
		
		move(first, d, -1, -1);
		int ax = isInHole(first) ? -1 : first.x;
		int ay = isInHole(first) ? -1 : first.y;
		move(second, d, ax, ay);
		
		return new MoveDTO(!isInHole(blue), new State(blue, red, cur.cnt+1));
	}
	
	static int bfs() {
		int res = Integer.MAX_VALUE;
		Queue<State> queue = new ArrayDeque<>();
		HashSet<String> visited = new HashSet<>();
		
		State start = new State(sbx, sby, srx, sry, 0);
		queue.add(start);
		visited.add(getStringCoord(start));
		
		while (!queue.isEmpty()) {
			State cur = queue.poll();
			if (cur.rx == hx && cur.ry == hy)
				return cur.cnt;
			
			if (cur.cnt == 10) continue;
			
			for (int i = 0; i < 4; i++) {
				MoveDTO nxt = move(cur, i);
				if (!nxt.isValid) continue;
				String nxtCoord = getStringCoord(nxt.state);
				if (visited.contains(nxtCoord)) continue;
				
				visited.add(nxtCoord);
				queue.add(nxt.state);
			}
		}
		
		return res != Integer.MAX_VALUE ? res : -1;
	}
}
