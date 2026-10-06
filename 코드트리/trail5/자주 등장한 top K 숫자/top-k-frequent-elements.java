import java.util.*;

class State implements Comparable<State> {
    int k, v;
    
    public State(int k, int v) {
        this.k = k;
        this.v = v;
    }

    public int compareTo(State o) {
        if (this.v == o.v) return Integer.compare(o.k, this.k);
        return Integer.compare(o.v, this.v);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            int k = sc.nextInt();
            int v = map.getOrDefault(k, 0);
            map.put(k, v+1);
        }
        TreeSet<State> states = new TreeSet<>();
        for (int k: map.keySet()) {
            states.add(new State(k, map.get(k)));
        }
        int cnt = 0;
        for (State s: states) {
            System.out.print(s.k + " ");
            if (++cnt == K) break;
        }
    }
}