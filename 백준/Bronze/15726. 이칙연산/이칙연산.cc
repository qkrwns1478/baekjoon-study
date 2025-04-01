#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    double d = (double) a * b / c;
    double e = (double) a / b * c;

    cout << (int) max(d, e) << endl;

    return 0;
}