class Solution {
    public String solution(String s) {
        StringBuilder res = new StringBuilder();
        String[] words = s.split(" ", -1);
        int N = words.length;
        for (int i = 0; i < N; i++) {
            String word = words[i];
            String postfix = i != N-1 ? " " : "";
            if (word.isBlank()) {
                res.append(word).append(postfix);
                continue;
            }
            char head = word.toUpperCase().charAt(0);
            String body = word.toLowerCase().substring(1);
            res.append(head).append(body).append(postfix);
        }
        return res.toString();
    }
}