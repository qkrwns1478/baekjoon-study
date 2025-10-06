import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        System.out.println(sol(input));
        scanner.close();
    }

    private static String sol(String s) {
        return switch (s) {
            case "fdsajkl;", "jkl;fdsa" -> "in-out";
            case "asdf;lkj", ";lkjasdf" -> "out-in";
            case "asdfjkl;" -> "stairs";
            case ";lkjfdsa" -> "reverse";
            default ->"molu";
        };
    }
}