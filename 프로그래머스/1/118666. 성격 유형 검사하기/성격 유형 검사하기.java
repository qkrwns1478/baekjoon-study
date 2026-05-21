class Solution {
    private int[] getIndex(String s) {
        return s.equals("RT") ? new int[]{0, 0, 1}
             : s.equals("TR") ? new int[]{0, 1, 0}
             : s.equals("CF") ? new int[]{1, 0, 1}
             : s.equals("FC") ? new int[]{1, 1, 0}
             : s.equals("JM") ? new int[]{2, 0, 1}
             : s.equals("MJ") ? new int[]{2, 1, 0}
             : s.equals("AN") ? new int[]{3, 0, 1}
             : new int[]{3, 1, 0};
    }
    
    public String solution(String[] survey, int[] choices) {
        String[] types = new String[]{"RT", "CF", "JM", "AN"};
        int[][] ind = new int[4][2];
        for (int i = 0; i < survey.length; i++) {
            int[] index = getIndex(survey[i]);
            int I = index[0], N = index[1], P = index[2];
            int C = choices[i];
            if (C == 1) ind[I][N] += 3;
            else if (C == 2) ind[I][N] += 2;
            else if (C == 3) ind[I][N] += 1;
            else if (C == 5) ind[I][P] += 1;
            else if (C == 6) ind[I][P] += 2;
            else if (C == 7) ind[I][P] += 3;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            if (ind[i][0] >= ind[i][1]) sb.append(types[i].charAt(0));
            else sb.append(types[i].charAt(1));
        }
        return sb.toString();
    }
}