class Solution {
    public int[] solution(int n, long left, long right) {
        int len = Math.toIntExact(right - left + 1);
        int[] res = new int[len];
        for (int i = 0; i < len; i++) {
            long cur = left + i;
            int a = Math.toIntExact(cur / n) + 1;
            int b = Math.toIntExact(cur % n) + 1;
            res[i] = Math.max(a, b);
        }
        return res;
    }
}