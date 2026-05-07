import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> rankByName = new HashMap<>();
        HashMap<Integer, String> rankByIndex = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            rankByName.put(players[i], i);
            rankByIndex.put(i, players[i]);
        }
        for (String cur: callings) {
            int idx = rankByName.get(cur);
            String prev = rankByIndex.get(idx-1);
            rankByName.put(prev, idx);
            rankByName.put(cur, idx-1);
            rankByIndex.put(idx, prev);
            rankByIndex.put(idx-1, cur);
        }
        String[] answer = new String[players.length];
        for (Integer key: rankByIndex.keySet()) {
            answer[key] = rankByIndex.get(key);
        }
        return answer;
    }
}