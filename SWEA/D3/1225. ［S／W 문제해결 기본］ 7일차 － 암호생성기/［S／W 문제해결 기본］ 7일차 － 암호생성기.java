import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Solution {
	private static Deque<Integer> deque;
	
	private static boolean rotate(int n) {
		Integer tmp = deque.poll() - n;
		tmp = tmp > 0 ? tmp : 0;
		deque.add(tmp);
		return tmp > 0;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for (int t = 1; t <= 10; t++) {
			sc.nextInt();
			
			deque = new ArrayDeque<>();
			for (int i = 0; i < 8; i++) {
				deque.add(sc.nextInt());
			}
			
			int n = 1;
			while (true) {
				boolean res = rotate(n);
				if (!res) break;
				if (++n == 6) n = 1;
			}
			
            System.out.print("#" + t + " ");
			for (int i = 0; i < 8; i++) {
				System.out.print(deque.poll() + " ");
			}
			System.out.println();
		}
		
		sc.close();
	}
}
