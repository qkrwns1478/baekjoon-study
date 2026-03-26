import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        String S = scanner.nextLine();
        StringBuilder R = new StringBuilder(N);
        for (char c: S.toCharArray()) {
            R.append(c);
            int M = R.length();
            if (M > 2 && R.charAt(M-1) == R.charAt(M-3)) {
                R.delete(M-3, M);
            } else if (M >= 2 && R.charAt(M-1) == R.charAt(M-2)) {
                R.delete(M-2, M);
            }
        }
        System.out.println(R.isEmpty() ? -1 : R.toString());
        scanner.close();
    }
}