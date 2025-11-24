import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] word = new int[26];
        while (scanner.hasNextLine()) {
            String s = scanner.nextLine();
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c != ' ') {
                    word[c - 'a']++;
                }
            }
        }
        int maxVal = 0;
        for (int i = 0; i < 26; i++) {
            if (word[i] > maxVal) {
                maxVal = word[i];
            }
        }
        for (int i = 0; i < 26; i++) {
            if (word[i] == maxVal) {
                System.out.print((char)(i + 'a'));
            }
        }
        scanner.close();
    }
}