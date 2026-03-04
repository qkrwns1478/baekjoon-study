import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        int S = 0, E = 0, ans = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        while (E < N) {
            map.put(arr[E], map.getOrDefault(arr[E], 0) + 1);
            while (map.size() > 2) {
                map.put(arr[S], map.getOrDefault(arr[S], 0) - 1);
                if (map.get(arr[S]) == 0) map.remove(arr[S]);
                S++;
            }
            E++;
            int sum = 0;
            for (var entry: map.entrySet()) {
                sum += entry.getValue();
            }
            ans = Math.max(ans, sum);
        }
        System.out.println(ans);
        scanner.close();
    }
}