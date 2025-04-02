#include <iostream>
#include <algorithm>

using namespace std;
int main() {
    int n, p;
    const int INF = 1000000000;
    int p1 = INF, p2 = INF, p3 = INF, p4 = INF;
    cin >> n;
    cin >> p;
    if (n >= 20) p1 = p * 0.75;
    if (n >= 15) p2 = p - 2000;
    if (n >= 10) p3 = p * 0.9;
    if (n >= 5) p4 = p - 500;

    p = min({p1, p2, p3, p4, p});
    if (p < 0) p = 0;
    cout << p << endl;

    return 0;
}