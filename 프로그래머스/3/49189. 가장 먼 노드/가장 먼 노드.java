import java.util.*;

class Solution {
    
    public int solution(int n, int[][] edge) {
        boolean[][] map = new boolean[n+1][n+1];
        for (int[] e: edge) {
            map[e[0]][e[1]] = true;
            map[e[1]][e[0]] = true;
        }
        boolean[] visited = new boolean[n+1];
        int[] dist = new int[n+1];
        Queue<Integer[]> queue = new LinkedList<>();
        queue.add(new Integer[]{1, 0});
        visited[1] = true;
        
        while (!queue.isEmpty()) {
            Integer[] cur = queue.poll();
            dist[cur[0]] = cur[1];
            for (int i = 1; i <= n; i++) {
                if (map[cur[0]][i] && !visited[i]) {
                    visited[i] = true;
                    queue.add(new Integer[]{i, cur[1] + 1});
                }
            }
        }
        
        Arrays.sort(dist);
        int max = dist[dist.length - 1];
        int answer = 0;
        for (int i = dist.length - 1; i >= 0; i--) {
            if (dist[i] == max) answer++;
            else break;
        }
        return answer;
    }
}