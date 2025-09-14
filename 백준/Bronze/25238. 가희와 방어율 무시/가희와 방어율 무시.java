import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputs[] = scanner.nextLine().split(" ");
        int a = Integer.parseInt(inputs[0]);
        int b = Integer.parseInt(inputs[1]);
        int c = (int) (a * (100-b) * 0.01);
        if (c >= 100)
            System.out.println(0);
        else
            System.out.println(1);
        scanner.close();
    }
}