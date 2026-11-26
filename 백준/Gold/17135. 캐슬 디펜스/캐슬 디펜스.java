import java.util.*;

class Entity {
	int x, y;

	public Entity(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Ranger extends Entity {
	public Ranger(int x, int y) {
		super(x, y);
	}
	
	public int getDist(int x, int y) {
		return Math.abs(this.x - x) + Math.abs(this.y - y);
	}
	
	public boolean isAttackable(int x, int y, int D) {
		return getDist(x, y) <= D;
	}
}

class Enemy extends Entity implements Comparable<Enemy> {
	int dist;
	
	public Enemy(int x, int y, int d) {
		super(x, y);
		this.dist = d;
	}

	@Override
	public int compareTo(Enemy o) {
		if (this.dist == o.dist) return Integer.compare(this.y, o.y);
		return Integer.compare(this.dist, o.dist);
	}
}

public class Main {
	static int N, M, D;
	static boolean[][] initMap;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		D = sc.nextInt();
		
		initMap = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				initMap[i][j] = sc.nextInt() == 1;
			}
		}
		
		int highScore = Integer.MIN_VALUE;
		for (int a = 0; a < M-2; a++) {
			for (int b = a+1; b < M-1; b++) {
				for (int c = b+1; c < M; c++) {
					highScore = Math.max(highScore, simulate(a, b, c));
				}
			}
		}
		
		System.out.println(highScore);
		sc.close();
	}
	
	static int simulate(int R1, int R2, int R3) {
		int score = 0;

		boolean[][] map = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				map[i][j] = initMap[i][j];
			}
		}
		
		List<Ranger> rangers = new ArrayList<>();
		rangers.add(new Ranger(N, R1));
		rangers.add(new Ranger(N, R2));
		rangers.add(new Ranger(N, R3));
		
		while (hasEnemy(map)) {
			Queue<Enemy> targets = new ArrayDeque<>();
			for (Ranger r: rangers) {
				PriorityQueue<Enemy> pq = new PriorityQueue<>();
				for (int i = N-1; i >= 0; i--) {
					for (int j = 0; j < M; j++) {
						if (map[i][j] && r.isAttackable(i, j, D)) {
							pq.offer(new Enemy(i, j, r.getDist(i, j)));
						}
					}
				}
				if (!pq.isEmpty()) targets.offer(pq.poll());
			}
			
			while (!targets.isEmpty()) {
				Enemy t = targets.poll();
				if (map[t.x][t.y]) {
					map[t.x][t.y] = false;
					score++;
				}
			}
			
			for (int j = 0; j < M; j++) {
				map[N-1][j] = false;
			}
			for (int i = N-2; i >= 0; i--) {
				for (int j = 0; j < M; j++) {
					if (map[i][j]) {
						map[i][j] = false;
						map[i+1][j] = true;
					}
				}
			}
		}
		
		return score;
	}
	
	static boolean hasEnemy(boolean[][] arr) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j]) return true;
			}
		}
		return false;
	}
}
