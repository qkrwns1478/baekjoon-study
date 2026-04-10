import java.util.*;

class Solution {
    private int[] A = new int[]{1, 2, 3, 4, 5};
    private int[] B = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
    private int[] C = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    public int[] solution(int[] answers) {

        int[][] pattern = new int[][]{
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        
        int[] score = new int[3];
        for (int i = 0; i < 3; i++) {
            int N = pattern[i].length;
            for (int j = 0; j < answers.length; j++) {
                score[i] += answers[j] == pattern[i][j % N] ? 1 : 0;
            }
        }
        
        int max = Arrays.stream(score).max().getAsInt();
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (score[i] == max) res.add(i+1);
        }
        
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}