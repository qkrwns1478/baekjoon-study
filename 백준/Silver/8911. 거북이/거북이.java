import java.util.Scanner;

public class Main {
    private static int minX, minY, maxX, maxY;

    public static void main(String[] args) {
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine();

        for (int t = 0; t < T; t++) {
            int x = 0, y = 0, d = 0;
            minX = 0; minY = 0; maxX = 0; maxY = 0;
            String s = scanner.nextLine();
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c == 'F') {
                    x += dx[d];
                    y += dy[d];
                    updateMinMax(x, y);
                } else if (c == 'B') {
                    x -= dx[d];
                    y -= dy[d];
                    updateMinMax(x, y);
                } else if (c == 'L') {
                    d = (d+1) % 4;
                } else { 
                    d = (d+3) % 4;
                }
            }
            System.out.println((maxX - minX) * (maxY - minY));
        }
        scanner.close();
    }
    
    private static void updateMinMax(int x, int y) {
        minX = Math.min(minX, x);
        minY = Math.min(minY, y);
        maxX = Math.max(maxX, x);
        maxY = Math.max(maxY, y);
    }
}