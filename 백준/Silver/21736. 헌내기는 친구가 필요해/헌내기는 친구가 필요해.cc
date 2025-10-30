#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<char>> arr(n, vector<char> (m));
    vector<vector<bool>> visited(n, vector<bool> (m));
    int sx, sy;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 'I') {
                sx = i;
                sy = j;
            }
        }
    }

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    int cnt = 0;
    queue<tuple<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = true;
    while(!q.empty()) {
        tuple cur = q.front();
        q.pop();
        int x, y;
        tie(x, y) = cur;
        if (arr[x][y] == 'P')
            cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (!visited[nx][ny] && arr[nx][ny] != 'X') {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
    }

    if (cnt == 0)
        cout << "TT" << endl;
    else
        cout << cnt << endl;
    return 0;
}