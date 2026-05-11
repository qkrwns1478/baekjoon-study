class Solution {
    public int[] solution(String s) {
        int cnt = 0, z = 0;
        while (!s.equals("1")) {
            int o = (int) s.chars().filter(c -> c == '1').count();
            z += s.length() - o;
            s = Integer.toBinaryString(o);
            cnt++;
        }

        return new int[]{cnt, z};
    }
}