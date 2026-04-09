import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int C = scanner.nextInt();
        int N = scanner.nextInt();
        if (C > N) System.out.println(0);
        else if (C < N) System.out.println(C+1);
        else System.out.println(N);
        scanner.close();
    }
}