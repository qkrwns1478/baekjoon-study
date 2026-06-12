import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Collections;
import java.util.Stack;

class Solution {
    public int solution(String s) {
        int n = s.length();
        
        List<Character> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(s.charAt(i));
        }
        
        LinkedList<Character> ll = new LinkedList<>(list);
        int answer = 0;
        for (int i = 0; i < n; i++) {
            Collections.rotate(ll, -1);
            
            Stack<Character> stack = new Stack<>();
            for (int j = 0; j < n; j++) {
                if (!stack.isEmpty()) {
                    if (stack.peek() == '[' && ll.get(j) == ']') stack.pop();
                    else if (stack.peek() == '(' && ll.get(j) == ')') stack.pop();
                    else if (stack.peek() == '{' && ll.get(j) == '}') stack.pop();
                    else stack.push(ll.get(j));
                } else stack.push(ll.get(j));
            }
            
            if (stack.isEmpty()) answer++;
        }
        
        return answer;
    }
}