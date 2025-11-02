#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <tuple>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> arr(n, vector<int>(m));
    int cheese = 0;
    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 1)
                cheese++;
        }
    }
    int cnt = 1;
    int answer;
    while (true) {
        queue<pair<int, int>> q0, q1;
        set<pair<int, int>> visited;
        q0.push({0, 0});
        visited.insert({0, 0});
        while (!q0.empty()) {
            auto [x, y] = q0.front();
            q0.pop();
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (visited.find({nx, ny}) == visited.end()) {
                        visited.insert({nx, ny});
                        if (arr[nx][ny] == 0) {
                            q0.push({nx, ny});
                        } else {
                            q1.push({nx, ny});
                        }
                    }
                }
            }
        }
        answer = q1.size();
        cheese -= answer;
        if (cheese == 0)
            break;
        while (!q1.empty()) {
            int x, y;
            tie(x, y) = q1.front();
            q1.pop();
            arr[x][y] = 0;
        }
        cnt++;
    }

    cout << cnt << endl;
    cout << answer << endl;
    return 0;
}