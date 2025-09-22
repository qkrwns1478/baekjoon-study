import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        HashMap<String, Integer> d = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String[] inputs = scanner.nextLine().split(" ");
            String a = inputs[0];
            String b = inputs[1];
            if (b.equals("enter")) {
                d.put(a, i);
            } else {
                d.remove(a);
            }
        }
        ArrayList<String> names = new ArrayList<>(d.keySet());
        names.sort(Collections.reverseOrder());
        for (String name: names) {
            System.out.println(name);
        }
        scanner.close();
    }
}