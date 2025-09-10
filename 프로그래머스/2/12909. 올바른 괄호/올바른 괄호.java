import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            stack.push(c);

            if (stack.size() >= 2) {
                char tmp = stack.pop();
                if (stack.peek() == '(' && tmp == ')') {
                    stack.pop();
                } else {
                    stack.push(tmp);
                }
            }
        }

        return stack.isEmpty();
    }
}