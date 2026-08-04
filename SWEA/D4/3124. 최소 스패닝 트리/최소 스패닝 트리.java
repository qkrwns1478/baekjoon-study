import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {
	int weight;
	int from;
	int to;
	
	public Edge(int weight, int from, int to) {
		this.weight = weight;
		this.from = from;
		this.to = to;
	}

	@Override
	public int compareTo(Edge o) {
		return this.weight - o.weight;
	}
}

public class Solution {
	private static int[] root;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			int V = sc.nextInt();
			int E = sc.nextInt();
			List<Edge> edges = new ArrayList<>(E);
			for (int i = 0; i < E; i++) {
				int A = sc.nextInt();
				int B = sc.nextInt();
				int C = sc.nextInt();
				edges.add(new Edge(C, A, B));
			}
			Collections.sort(edges);
			
			root = new int[V+1];
			for (int i = 1; i <= V; i++) {
				root[i] = i;
			}
			
			long total = 0;
			int selected = 0;
			for (Edge edge: edges) {
				if (union(edge)) {
					total += edge.weight;
					selected++;
					if (selected == V-1)
						break;
				}
			}
			
			System.out.println("#" + t + " " + total);
		}
		
		sc.close();
	}
	
	private static boolean union(Edge e) {
		int rootFrom = find(e.from);
		int rootTo = find(e.to);
		if (rootFrom == rootTo) return false;
		
		root[rootTo] = rootFrom;
		return true;
	}
	
	private static int find(int x) {
		if (root[x] == x)
			return x;
		else
			return root[x] = find(root[x]);
	}
}
