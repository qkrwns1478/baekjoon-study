import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String line = scanner.nextLine();
            String[] buf = line.split(" ", 2);
            char x = buf[0].charAt(0);
            if (x == '#')
                break;
            String text = buf[1].toLowerCase();
            int cnt = 0;
            for (int i = 0; i < text.length(); i++) {
                if (text.charAt(i) == x)
                    cnt++;
            }
            System.out.println(buf[0] + " " + cnt);
        }
        scanner.close();
    }
}