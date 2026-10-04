import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Map<String, String> mapSI = new HashMap<>();
        Map<String, String> mapIS = new HashMap<>();
        // Please write your code here.
        for (int i = 1; i <= n; i++) {
            String s = sc.next();
            mapSI.put(s, String.valueOf(i));
            mapIS.put(String.valueOf(i), s);
        }
        for (int i = 0; i < m; i++) {
            String input = sc.next();
            if (mapSI.keySet().contains(input))
                System.out.println(mapSI.get(input));
            else if (mapIS.keySet().contains(input))
                System.out.println(mapIS.get(input));
        }
    }
}