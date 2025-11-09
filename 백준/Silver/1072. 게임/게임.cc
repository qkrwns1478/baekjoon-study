#include <iostream>
using namespace std;

int get_z(long long x, long long y) {
    return (100 * y) / x;
}

int main() {
    long long x, y;
    cin >> x >> y;
    int z = get_z(x, y);
    long long l = 0, r = x;
    long long answer = -1;
    if (z < 99) {
        while (l <= r) {
            long long m = (l + r) / 2;
            if (get_z(x + m, y + m) > z) {
                answer = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
    }
    cout << answer << endl;
    return 0;
}