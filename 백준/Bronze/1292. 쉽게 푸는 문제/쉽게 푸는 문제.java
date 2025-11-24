import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int A = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 1; i < 47; i++) {
            for (int j = 0; j < i; j++) {
                arr.add(i);
            }
        }
        int answer = 0;
        for (int i = A-1; i < B; i++) {
            answer += arr.get(i);
        }
        System.out.println(answer);
        scanner.close();
    }
}