import java.util.*;

public class Main {
    static HashMap<Integer, Integer> map;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int k = sc.nextInt();
            int v = getValue(k);
            map.put(k, v+1);
        }

        for (int i = 0; i < m; i++) {
            int q = sc.nextInt();
            System.out.print(getValue(q) + " ");
        }
        // Please write your code here.
    }

    static int getValue(int k) {
        return map.keySet().contains(k) ? map.get(k) : 0;
    }
}