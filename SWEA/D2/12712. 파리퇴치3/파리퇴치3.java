import java.util.Scanner;

class Solution
{
    private static final int[] dxA = {1, 0, -1, 0};
    private static final int[] dyA = {0, 1, 0, -1};
    private static final int[] dxB = {1, 1, -1, -1};
    private static final int[] dyB = {1, -1, 1, -1};

    private static boolean isValid(int x, int y, int N) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }

    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {

            /////////////////////////////////////////////////////////////////////////////////////////////
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[][] arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            long res = 0;
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    long sumA = arr[x][y];
                    for (int i = 0; i < 4; i++) {
                        int nx = x, ny = y;
                        for (int j = 1; j < M; j++) {
                            nx += dxA[i];
                            ny += dyA[i];
                            if (!isValid(nx, ny, N)) break;
                            sumA += arr[nx][ny];
                        }
                    }
                    long sumB = arr[x][y];
                    for (int i = 0; i < 4; i++) {
                        int nx = x, ny = y;
                        for (int j = 1; j < M; j++) {
                            nx += dxB[i];
                            ny += dyB[i];
                            if (!isValid(nx, ny, N)) break;
                            sumB += arr[nx][ny];
                        }
                    }
                    res = Math.max(res, Math.max(sumA, sumB));
                }
            }

            System.out.println("#" + test_case + " " + res);
            /////////////////////////////////////////////////////////////////////////////////////////////

        }
    }
}
