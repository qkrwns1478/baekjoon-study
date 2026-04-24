import java.util.*;

public class Main {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int A = Integer.parseInt(input[0].replaceAll("5", "6"));
        int a = Integer.parseInt(input[0].replaceAll("6", "5"));
        int B = Integer.parseInt(input[1].replaceAll("5", "6"));
        int b = Integer.parseInt(input[1].replaceAll("6", "5"));
        System.out.println((a+b) + " " +(A+B));

    }
}