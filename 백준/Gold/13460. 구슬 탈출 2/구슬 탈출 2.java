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
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		sc.nextLine();
		
		isBlocked = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			String s = sc.nextLine();
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
		sc.close();
	}
	
	static boolean isInRange(int x, int y) {
		return 0 <= x && x < N && 0 <= y && y < M;
	}
	
	static String getStringCoord(int bx, int by, int rx, int ry) {
		return String.format("%d,%d,%d,%d", bx, by, rx, ry);
	}
	
	static String getStringCoord(State s) {
		return getStringCoord(s.bx, s.by, s.rx, s.ry);
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
		
		return new MoveDTO(!isInHole(blue), new State(blue.x, blue.y, red.x, red.y, cur.cnt+1));
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
	
	static boolean isInHole(Marble m) {
		return m.x == hx && m.y == hy;
	}
	
	static int bfs() {
		int res = Integer.MAX_VALUE;
		Queue<State> queue = new ArrayDeque<>();
		HashSet<String> visited = new HashSet<>();
		queue.add(new State(sbx, sby, srx, sry, 0));
		visited.add(getStringCoord(sbx, sby, srx, sry));
		
		while (!queue.isEmpty()) {
			State cur = queue.poll();
			if (cur.rx == hx && cur.ry == hy) {
//				res = Math.min(res, cur.cnt);
//				continue;
				return cur.cnt;
			}
			
			if (cur.cnt == 10) continue;
			
			/*
			for (int i = 0; i < 4; i++) {
				int nbx = cur.bx + dx[i];
				int nby = cur.by + dy[i];
				if (!isInRange(nbx, nby)) continue;
				if (isBlocked[nbx][nby]) continue;
				// 파란 구슬은 구멍에 들어가면 안됨
				if (nbx == hx && nby == hy) continue;
				
				for (int j = 0; j < 4; j++) {
					int nrx = cur.rx + dx[j];
					int nry = cur.ry + dy[j];
					if (!isInRange(nrx, nry)) continue;
					String nxtCoord = getStringCoord(nbx, nby, nrx, nry);
					if (visited.contains(nxtCoord))
					if (isBlocked[nrx][nry]) continue;
					
					visited.add(nxtCoord);
					queue.add(new State(nbx, nby, nrx, nry, cur.cnt+1));
				}
			}
			*/
			
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
