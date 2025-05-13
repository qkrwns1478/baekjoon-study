#include <iostream>
using namespace std;
int main() {
    int a, b, c, d;
    int w, x, y, z;
    cin >> a >> b >> c >> d;
    cin >> w >> x >> y >> z;
    int S = a + b + c + d;
    int T = w + x + y + z;
    if (S >= T) cout << S << endl;
    else cout << T << endl;
    return 0;
}