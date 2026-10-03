import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String k = sc.next();
            int v = map.keySet().contains(k) ? map.get(k) : 0;
            map.put(k, v+1);
        }

        int maxVal = 0;
        for (String k: map.keySet()) {
            maxVal = Math.max(maxVal, map.get(k));
        }
        System.out.println(maxVal);
    }
}