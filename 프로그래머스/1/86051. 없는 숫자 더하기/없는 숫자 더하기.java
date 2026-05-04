import java.util.HashSet;

class Solution {
    public int solution(int[] numbers) {
        HashSet<Integer> set = new HashSet<>();
        for (int n: numbers) {
            set.add(n);
        }
        int res = 0;
        for (int i = 0; i <= 9; i++) {
            if (!set.contains(i)) res += i;
        }
        return res;
    }
}