import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			String s = sc.nextLine();
			if(s.equals("END")) break;
			
			if (s.matches("\"([A-Z][A-Z ]*[A-Z]?)\" \\1"))
				System.out.println("Quine(" + s.substring(s.lastIndexOf("\"")+2) + ")");
			else
				System.out.println("not a quine");
		}
		sc.close();
	}
}
