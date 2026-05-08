class Solution {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, -1, 1, 0};
        String[] nd = {"d", "l", "r", "u"};
        int sx = x-1, sy = y-1, ex = r-1, ey = c-1;
        
        StringBuilder sb = new StringBuilder();
        int curX = sx, curY = sy;

        for (int i = 0; i < k; i++) {
            boolean flag = false;
            for (int j = 0; j < 4; j++) {
                int nx = curX + dx[j], ny = curY + dy[j];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    int dist = Math.abs(nx-ex) + Math.abs(ny-ey);
                    int rem = k - (i+1);
                    if (dist <= rem && (rem-dist) % 2 == 0) {
                        curX = nx;
                        curY = ny;
                        sb.append(nd[j]);
                        flag = true;
                        break;
                    }
                }
            }
            if (!flag) return "impossible";
        }
        
        return sb.toString();
    }
}