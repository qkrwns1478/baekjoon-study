import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        String[] words = scanner.nextLine().split(" ");

        char C = words[0].charAt(0);
        boolean flag = true;
        for (int i = 0; i < N; i++) {
            if (words[i].charAt(0) != C) {
                flag = false;
                break;
            }
        }

        System.out.println(flag ? 1 : 0);
        scanner.close();
    }
}