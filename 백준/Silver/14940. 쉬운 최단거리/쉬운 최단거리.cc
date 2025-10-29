#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int sx, sy;
    vector<vector<int>> arr(n, vector<int>(m));
    vector<vector<int>> visited(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 0) {
                visited[i][j] = 0;
            } else if (arr[i][j] == 2) {
                visited[i][j] = 0;
                sx = i;
                sy = j;
            } else
                visited[i][j] = -1;
        }
    }

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    queue<tuple<int, int, int>> queue;
    queue.push({sx, sy, 0});
    while (!queue.empty()) {
        tuple cur = queue.front();
        queue.pop();
        int x, y, cnt;
        tie(x, y, cnt) = cur;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < m)
                if (visited[nx][ny] == -1) {
                    visited[nx][ny] = cnt + 1;
                    queue.push({nx, ny, cnt + 1});
                }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << visited[i][j] << ' ';
        }
        if (i != n-1)
            cout << endl;
    }

    return 0;
}