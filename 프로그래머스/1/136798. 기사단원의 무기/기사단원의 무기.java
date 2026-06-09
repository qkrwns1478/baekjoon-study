class Solution {
    private int countDivisors(int n) {
        int res = 0;
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                res += i * i == n ? 1 : 2;
            }
        }
        return res;
    }
    
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            int cur = countDivisors(i);
            if (cur > limit) cur = power;
            answer += cur;
        }
        return answer;
    }
}