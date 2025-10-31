#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int dist(int r1, int c1, int r2, int c2) {
    return abs(r1 - r2) + abs(c1 - c2);
}

void generateCombinations(int s, int cnt, int m, int c, vector<int> &cur, vector<vector<int>> &res) {
    if (cnt == m) {
        res.push_back(cur);
        return;
    }
    for (int i = s; i < c; i++) {
        cur.push_back(i);
        generateCombinations(i + 1, cnt + 1, m, c, cur, res);
        cur.pop_back();
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> house, chicken;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int tmp;
            cin >> tmp;
            if (tmp == 1) {
                house.push_back({i, j});
            } else if (tmp == 2) {
                chicken.push_back({i, j});
            }
        }
    }

    int h = house.size();
    int c = chicken.size();
    vector<vector<int>> arr(h, vector<int>(c));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < c; j++) {
            arr[i][j] = dist(house[i].first, house[i].second, chicken[j].first, chicken[j].second);
        }
    }

    vector<vector<int>> cmbs;
    vector<int> cur;
    generateCombinations(0, 0, m, c, cur, cmbs);

    int answer = INT_MAX;
    for (const auto &cmb: cmbs) {
        int cur = 0;
        for (int i = 0; i < h; i++) {
            int c_dist = INT_MAX;
            for (int j: cmb) {
                c_dist = min(c_dist, arr[i][j]);
            }
            cur += c_dist;
        }
        answer = min(answer, cur);
    }
    cout << answer << endl;
    return 0;
}