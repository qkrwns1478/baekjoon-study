import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        scanner.nextLine();
        String[] arrStr = scanner.nextLine().split(" ");
        int[] arr = new int[a];
        for (int i = 0; i < a; i++) {
            arr[i] = Integer.parseInt(arrStr[i]);
        }
        int b = scanner.nextInt();

        long x = 0;
        for (int i = 0; i < a; i++) {
            if (arr[i] != 0 && arr[i] <= b)
                x++;
            else if (arr[i] != 0 && arr[i] > b) {
                if (arr[i] % b != 0)
                    x += (arr[i]/b) + 1;
                else
                    x += (arr[i]/b);
            }
        }
        System.out.println((long)b * x);
        scanner.close();
    }
}