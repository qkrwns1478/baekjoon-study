#include <iostream>
using namespace std;
int main() {
    int a, b, c;
    char d, e;
    cin >> a >> d >> b >> e >> c;
    if (a+b == c) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}