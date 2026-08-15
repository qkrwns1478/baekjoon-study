import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 0; t < T; t++) {
			int N = sc.nextInt(); // V = N
			int M = N * (N-1) / 2;
			List<Long> wList = new ArrayList<>();
			for (int i = 0; i < M; i++) {
				wList.add(sc.nextLong());
			}
			Collections.sort(wList);
			
			long minCost = 0;
			for (int i = 0; i < N-1; i++) {
				minCost += wList.get(i);
			}
			
			long maxCost = 0;
			int level = 0;
			int idx = 0;
			while (level < N-1) {
				maxCost += wList.get(idx);
				level++;
				idx += level;
			}
			System.out.println(minCost + " " + maxCost);
		}
		sc.close();
	}
}
