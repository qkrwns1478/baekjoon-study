import java.util.*;

public class Main {
	static final int INF = Integer.MAX_VALUE;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[][] map = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = i == j ? 0 : INF;
			}
		}
		
		while (true) {
			int X = sc.nextInt();
			int Y = sc.nextInt();
			if (X == -1 && Y == -1) break;
			map[X-1][Y-1] = 1;
			map[Y-1][X-1] = 1;
		}
		
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][k] == INF || map[k][j] == INF) continue;
					map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
				}
			}
		}
		
		int minScore = INF;
		int[] scores = new int[N];
		for (int i = 0; i < N; i++) {
			int cur = 0;
			for (int j = 0; j < N; j++) {
				cur = Math.max(cur, map[i][j]);
			}
			minScore = Math.min(minScore, cur);
			scores[i] = cur;
		}
		
		Set<Integer> answer = new TreeSet<>();
		for (int i = 0; i < N; i++) {
			if (scores[i] == minScore) answer.add(i+1);
		}
		
		System.out.println(minScore + " " + answer.size());
		System.out.println(answer.toString().replaceAll(",", "").replace("[", "").replace("]", ""));
		
		sc.close();
	}
}
