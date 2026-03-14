import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, String> dict = new HashMap<>();
        String[] words = {
            "CU", "see you",
            ":-)", "I’m happy",
            ":-(", "I’m unhappy",
            ";-)", "wink",
            ":-P", "stick out my tongue",
            "(~.~)", "sleepy",
            "TA", "totally awesome",
            "CCC", "Canadian Computing Competition",
            "CUZ", "because",
            "TY", "thank-you",
            "YW", "you’re welcome",
            "TTYL", "talk to you later"
        };
        for (int i = 0; i < words.length; i+=2) {
            dict.put(words[i], words[i+1]);
        }
        while (true) {
            String input = scanner.nextLine();
            System.out.println(dict.getOrDefault(input, input));
            if (input.equals("TTYL")) break;
        }
        scanner.close();
    }
}