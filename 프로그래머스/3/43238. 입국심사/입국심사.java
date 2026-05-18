import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long left = times[0];
        long right = times[times.length - 1] * (long) n;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            long cur = 0;
            for (int time: times) {
                cur += mid / time;
                if (cur >= n) break;
            }
            if (cur >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return answer;
    }
}