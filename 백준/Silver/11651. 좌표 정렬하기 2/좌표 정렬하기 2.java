import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Point implements Comparable<Point> {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point other) {
        if (this.y != other.y) {
            return Integer.compare(this.y, other.y);
        }
        return Integer.compare(this.x, other.x);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();

        ArrayList<Point> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] inputs = scanner.nextLine().split(" ");
            int x = Integer.parseInt(inputs[0]);
            int y = Integer.parseInt(inputs[1]);
            arr.add(new Point(x, y));
        }

        Collections.sort(arr);
        for (int i = 0; i < N; i++) {
            Point p = arr.get(i);
            System.out.println(p.x + " " + p.y);
        }
        scanner.close();
    }
}