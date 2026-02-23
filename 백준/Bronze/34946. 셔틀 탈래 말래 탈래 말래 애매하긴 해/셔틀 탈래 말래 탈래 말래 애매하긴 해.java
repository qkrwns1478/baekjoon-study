import java.util.Base64;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        int D = scanner.nextInt();
        boolean bus = (A+B) <= D;
        boolean walk = C <= D;
        String ans;
        if (bus && walk) ans = "fi5+";
        else if (!bus && !walk) ans = "VC5U";
        else if (bus) ans = "U2h1dHRsZQ==";
        else ans = "V2Fsaw==";
        System.out.println(new String(Base64.getDecoder().decode(ans)));
        scanner.close();
    }
}