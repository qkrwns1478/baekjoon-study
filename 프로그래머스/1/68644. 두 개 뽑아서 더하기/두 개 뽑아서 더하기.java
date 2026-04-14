import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        boolean[] B = new boolean[201];
        Arrays.sort(numbers);
        int n = numbers.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                B[numbers[i] + numbers[j]] = true;
            }
        }
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < 201; i++) {
            if (B[i]) arr.add(i);
        }
        int[] res = arr.stream().mapToInt(i -> i).toArray();
        Arrays.sort(res);
        return res;
    }
}