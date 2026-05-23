import java.util.Scanner;

class Solution {
    static int N;
    static int[][] customers;
    static int compX, compY, houseX, houseY;
    static boolean[] visited;
    static int minDist;

    private static int getDist(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            compX = sc.nextInt();
            compY = sc.nextInt();
            houseX = sc.nextInt();
            houseY = sc.nextInt();

            customers = new int[N][2];
            for (int i = 0; i < N; i++) {
                customers[i][0] = sc.nextInt();
                customers[i][1] = sc.nextInt();
            }

            visited = new boolean[N];
            minDist = Integer.MAX_VALUE;
            solution(0, compX, compY, 0);

            System.out.println("#" + test_case + " " + minDist);
        }
    }

    static void solution(int count, int curX, int curY, int sumDist) {
        if (sumDist >= minDist) return;

        if (count == N) {
            int finalDist = sumDist + getDist(curX, curY, houseX, houseY);
            minDist = Math.min(minDist, finalDist);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                int nextDist = getDist(curX, curY, customers[i][0], customers[i][1]);
                solution(count+1, customers[i][0], customers[i][1], sumDist + nextDist);
                visited[i] = false;
            }
        }
    }
}