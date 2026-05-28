class Solution {
    public boolean solution(int x) {
        int X = x;
        int N = 0;
        while (X > 0) {
            N += (X % 10);
            X /= 10;
        }
        return x % N == 0;
    }
}