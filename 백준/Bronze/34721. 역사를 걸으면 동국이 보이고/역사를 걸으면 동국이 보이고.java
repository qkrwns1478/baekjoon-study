import java.util.Base64;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String code = "NzNfMzJfMTA4XzExMV8xMThfMTAxXzMyXzY4XzcxXzg1";
        byte[] decodedBytes = Base64.getDecoder().decode(code);
        String decodedString = new String(decodedBytes);
        String[] strArr = decodedString.split("_");

        int[] arr = new int[strArr.length];
        for (int i = 0; i < strArr.length; i++) {
            arr[i] = Integer.parseInt(strArr[i]);
        }

        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            int N = scanner.nextInt();
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < arr.length; j++) {
                    System.out.print((char) arr[j]);
                }
                System.out.println();
            }
        }
        scanner.close();
    }
}