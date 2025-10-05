import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            ArrayList<double[]> arr = new ArrayList<>();

            for (int j = 0; j < n; j++) {
                double w = scanner.nextDouble();
                double c = scanner.nextDouble();
                arr.add(new double[]{w, c, c / w});
            }

            arr.sort((o1, o2) -> {
                if (o1[2] != o2[2]) {
                    return Double.compare(o1[2], o2[2]);
                } else {
                    return Double.compare(o1[1], o2[1]);
                }
            });

            System.out.println((int)arr.get(0)[1]);
        }
        scanner.close();
    }
}