#include <iostream>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    int a = 100 - n;
    int b = 100 - m;
    int c = 100 - (a+b);
    int d = a * b;
    int q = d / 100;
    int r = d % 100;
    cout << a << ' ' << b << ' ' << c << ' ' << d << ' ' << q << ' ' << r << endl;
    if (d >= 100) cout << c+q << ' ' << r;
    else cout << c << ' ' << d;
    return 0;
}