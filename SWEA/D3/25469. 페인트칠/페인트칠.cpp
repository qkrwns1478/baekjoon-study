#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, m;
        cin >> n >> m;
        int arr[n][m];
        for (int i = 0; i < n; i++) {
            string tmp;
            cin >> tmp;
            for (int j = 0; j < m; j++) {
                arr[i][j] = (tmp[j] == '#' ? 1 : 0);
            }
        }

        int cntR = 0;
        int cntC = 0;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < m; j++) {
                sum += arr[i][j];
            }
            if (sum == m) cntR++;
        }
        for (int j = 0; j < m; j++) {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += arr[i][j];
            }
            if (sum == n) cntC++;
        }

        int answer = (cntR == n && cntC == m) ? min(cntR, cntC) : cntR + cntC;
        cout << answer << endl;
    }
    return 0;
}