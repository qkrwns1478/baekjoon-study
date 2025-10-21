import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextLine();
        }

        boolean isIncreasing = true;
        boolean isDecreasing = true;
        for (int i = 0; i < n-1; i++) {
            if (arr[i].compareTo(arr[i+1]) < 0) {
                isDecreasing = false;
            } else {
                isIncreasing = false;
            }
        }

        if (isIncreasing) {
            System.out.println("INCREASING");
        } else if (isDecreasing) {
            System.out.println("DECREASING");
        } else {
            System.out.println("NEITHER");
        }
        scanner.close();
    }
}