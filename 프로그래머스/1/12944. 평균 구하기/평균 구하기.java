class Solution {
    public double solution(int[] arr) {
        return java.util.Arrays.stream(arr).average().orElse(0.0);
    }
}