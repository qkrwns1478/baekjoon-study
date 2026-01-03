import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int mileage = 0;
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("#"))
                break;
            else if (input.equals("0")) {
                System.out.println(mileage);
                mileage = 0;
            } else {
                String[] inputs = input.split(" ");
                String classCode = inputs[3];
                double bonus = 1;
                if (classCode.equals("F")) bonus = 2;
                else if (classCode.equals("B")) bonus = 1.5;
                int m = Integer.parseInt(inputs[2]);
                if (bonus == 1 && m <= 500) m = 500;
                mileage += (int) Math.round(bonus * m);
            }
        }
        scanner.close();
    }
}