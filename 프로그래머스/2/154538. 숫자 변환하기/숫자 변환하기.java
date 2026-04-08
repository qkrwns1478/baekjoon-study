import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        Queue<int[]> queue = new ArrayDeque<>();
        HashSet<String> visited = new HashSet<>();
        queue.add(new int[]{x, 0});
        visited.add(String.valueOf(x));

        while (!queue.isEmpty()) {
            int[] pop = queue.poll();
            int cur = pop[0], cnt = pop[1];
            if (cur == y) return cnt;
            int[] nxt = {cur * 3, cur * 2, cur + n};
            for (int i = 0; i < 3; i++) {
                if (nxt[i] <= y && !visited.contains(String.valueOf(nxt[i]))) {
                    visited.add(String.valueOf(nxt[i]));
                    queue.add(new int[]{nxt[i], cnt+1});
                }
            }
        }
        return -1;
    }
}