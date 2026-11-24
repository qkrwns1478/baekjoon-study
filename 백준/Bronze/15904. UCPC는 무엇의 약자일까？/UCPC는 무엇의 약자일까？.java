import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		char[] chars = {'U', 'C', 'P', 'C'};
		int idx = 0;
		
		Deque<Character> deque = new ArrayDeque<>();
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == chars[idx]) {
				deque.offer(c);
				if (++idx == 4)
					break;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (char c: deque) sb.append(c);
		String res = sb.toString();
		
		String target = "UCPC";
		String prefix = target.equals(res) ? "I love" : "I hate";
		System.out.println(prefix + " " + target);
		sc.close();
	}
}
