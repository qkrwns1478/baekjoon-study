import java.util.*;

class Block implements Comparable<Block> {
	int totalSize, rBlocks, minR, minC;
	Set<Integer[]> coords;
	
	public Block(int totalSize, int rBlocks, int minR, int minC) {
		this.totalSize = totalSize;
		this.rBlocks = rBlocks;
		this.minR = minR;
		this.minC = minC;
		coords = new HashSet<>();
	}
	
	public int getScore() {
		return this.totalSize * this.totalSize;
	}
	
	@Override
	public int compareTo(Block o) {
		if (this.totalSize == o.totalSize) {
			if (this.rBlocks == o.rBlocks) {
				if (this.minR == o.minR) {
					return Integer.compare(o.minC, this.minC);
				}
				return Integer.compare(o.minR, this.minR);
			}
			return Integer.compare(o.rBlocks, this.rBlocks);
		}
		return Integer.compare(o.totalSize, this.totalSize);
	}
	
}

public class Main {
	static final int NULL = -2;
	
	static int N, M, arr[][];
	static boolean[][] visited;
	static Block curBlock;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		int totalScore = 0;
		
		while (true) {
			PriorityQueue<Block> pq = new PriorityQueue<>();
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (arr[i][j] > 0) {
						visited = new boolean[N][N];
						visited[i][j] = true;
						
						curBlock = new Block(1, 0, i, j);
						curBlock.coords.add(new Integer[] {i, j});
						
						dfs(i, j, arr[i][j]);
						if (curBlock.totalSize >= 2) {
							pq.offer(curBlock);
						}
					}
				}
			}
			
			if (pq.isEmpty()) break;
			
			Block b = pq.poll();
			totalScore += b.getScore();
			for (Integer[] coord: b.coords) {
				arr[coord[0]][coord[1]] = NULL;
			}
			
			gravity();
			rotate();
			gravity();
		}
		
		System.out.println(totalScore);
		sc.close();
	}
	
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	
	static void dfs(int x, int y, int v) {
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if (!isInRange(nx, ny)) continue;
			if (arr[nx][ny] != 0 && arr[nx][ny] != v) continue;
			if (visited[nx][ny]) continue;
			
			
			if (arr[nx][ny] == v) {
				curBlock.minR = Math.min(curBlock.minR, nx);
				curBlock.minC = Math.min(curBlock.minC, ny);
			} else {
				curBlock.rBlocks++;
			}
			
			visited[nx][ny] = true;
			curBlock.totalSize++;
			curBlock.coords.add(new Integer[] {nx, ny});
			dfs(nx, ny, v);
		}
	}
	
	static boolean isInRange(int x, int y) {
		return 0 <= x && x < N && 0 <= y && y < N;
	}
	
	static void gravity() {
		for (int j = 0; j < N; j++) {
			int k = N-1;
			for (int i = N-1; i >= 0; i--) {
				if (arr[i][j] == -1) {
					k = i-1;
				} else if (arr[i][j] != NULL) {
					arr[k][j] = arr[i][j];
					if (k != i) arr[i][j] = NULL;
					k--;
				}
			}
		}
	}
	
	static void rotate() {
		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				int tmp = arr[i][j];
				arr[i][j] = arr[j][i];
				arr[j][i] = tmp;
			}
		}
		
		for (int j = 0; j < N; j++) {
			for (int i = 0; i < N/2; i++) {
				int tmp = arr[i][j];
				arr[i][j] = arr[N-1-i][j];
				arr[N-1-i][j] = tmp;
			}
		}
	}
}
