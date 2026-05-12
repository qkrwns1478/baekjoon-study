class Solution {
    public int[] solution(int brown, int yellow) {
        int b = (brown + 4) / 2;
        int c = brown + yellow;
        double D = Math.sqrt(b * b - 4 * c);
        int r1 = (int) (b + D) / 2;
        int r2 = (int) (b - D) / 2;
        return new int[]{r1, r2};
    }
}