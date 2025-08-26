import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] p1 = readPoints(scanner);
        int[] p2 = readPoints(scanner);
        int[] p3 = readPoints(scanner);

        int ccw = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1]);
        int answer = -1;
        if (ccw > 0) answer = 1;
        else if (ccw == 0) answer = 0;
        System.out.println(answer);
        scanner.close();
    }

    private static int[] readPoints(Scanner scanner) {
        String inputLine = scanner.nextLine();
        String[] inputNums = inputLine.split(" ");
        int x = Integer.parseInt(inputNums[0]);
        int y = Integer.parseInt(inputNums[1]);
        return new int[]{x, y};
    }
}