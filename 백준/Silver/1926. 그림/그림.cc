#include <iostream>
#include <vector>
#include <set>
#include <tuple>
using namespace std;

int n, m;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
set<tuple<int, int>> visited;

int dfs(int x, int y, int size, vector<vector<int>> &arr) {
    int res = 1;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            if (arr[nx][ny] == 1 && !visited.count({nx, ny})) {
                visited.insert({nx, ny});
                res += dfs(nx, ny, size+1, arr);
            }
        }
    }
    return res;
}

int main() {
    cin >> n >> m;
    vector<vector<int>> arr(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    int size = 0;
    int answer = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 1 && !visited.count({i, j})) {
                visited.insert({i, j});
                answer = max(answer, dfs(i, j, 1, arr));
                size++;
            }
        }
    }
    cout << size << endl << answer << endl;

    return 0;
}