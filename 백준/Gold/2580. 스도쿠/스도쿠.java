import java.util.ArrayList;
import java.util.Scanner;

class Node {
    int x;
    int y;
    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
    int getX() {
        return this.x;
    }
    int getY() {
        return this.y;
    }
}

public class Main {
    static int[][] arr = new int[9][9];
    static ArrayList<Node> zeros = new ArrayList<>();

    private static Boolean isValid(int x, int y, int n) {
        for (int j = 0; j < 9; j++) {
            if (arr[x][j] == n)
                return false;
        }
        for (int i = 0; i < 9; i++) {
            if (arr[i][y] == n)
                return false;
        }
        int sx = 3 * (x/3);
        int sy = 3 * (y/3);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (arr[sx+i][sy+j] == n)
                    return false;
            }
        }
        return true;
    }

    private static void dfs(int z) {
        if (z == zeros.size()) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.printf("%d ", arr[i][j]);
                }
                System.out.print("\n");
            }
            System.exit(0);
        }
        int x = zeros.get(z).getX();
        int y = zeros.get(z).getY();
        for (int i = 1; i < 10; i++) {
            if (isValid(x, y, i)) {
                arr[x][y] = i;
                dfs(z+1);
                arr[x][y] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                arr[i][j] = scanner.nextInt();
                if (arr[i][j] == 0) {
                    zeros.add(new Node(i, j));
                }
            }
        }
        dfs(0);
        scanner.close();
    }
}