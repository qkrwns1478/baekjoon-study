class Solution {

    static int N;
    static int[][] coms;
    static boolean[] visited;

    private void dfs(int x) {
        visited[x] = true;
        for (int i = 0; i < N; i++) {
            if (coms[x][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public int solution(int n, int[][] computers) {
        int answer = 0;
        N = n;
        coms = computers;
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                dfs(i);
                answer++;
            }
        }

        return answer;
    }
}