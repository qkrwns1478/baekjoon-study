import java.util.*;

class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int n = p.length();
        StringBuilder sb = new StringBuilder(t);
        for (int i = 0; i < t.length() - n + 1; i++) {
            String cur = sb.substring(i, i + n);
            // System.out.println(cur);
            if (Long.parseLong(cur) <= Long.parseLong(p)) answer++;
        }
        
        return answer;
    }
}