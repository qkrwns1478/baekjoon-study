import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] lpStr = scanner.nextLine().split(" ");
        int l = Integer.parseInt(lpStr[0]);
        int p = Integer.parseInt(lpStr[1]);

        String[] arrStr = scanner.nextLine().split(" ");
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = Integer.parseInt(arrStr[i]);
        }
        
        for (int i = 0; i < 5; i++) {
	System.out.printf("%d ", arr[i] - (l*p));
        }
    }
}