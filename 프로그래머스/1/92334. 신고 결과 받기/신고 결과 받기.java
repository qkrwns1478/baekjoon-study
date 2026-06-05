import java.util.HashMap;

class Solution {
    public int[] solution(String[] id_list, String[] reports, int k) {
        int n = id_list.length;
        boolean[][] map = new boolean[n][n];
        
        HashMap<String, Integer> hash = new HashMap<>();
        for (int i = 0; i < n; i++) {
            hash.put(id_list[i], i);
        }
        
        for (String report: reports) {
            String[] tmp = report.split(" ");
            String a = tmp[0];
            String b = tmp[1];
            map[hash.get(a)][hash.get(b)] = true;
        }
        
        boolean[] black_list = new boolean[n];
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = 0; j < n; j++) {
                cur += map[j][i] ? 1 : 0;
            }
            if (cur >= k)
                black_list[i] = true;
        }
        
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (black_list[j])
                    answer[i] += map[i][j] ? 1 : 0;
            }
        }
        return answer;
    }
}