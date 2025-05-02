#include <iostream>
using namespace std;
int main() {
    int s, t, d;
    cin >> s >> t >> d;
    int h = d / (s * 2);
    cout << h * t << endl;
    return 0;
}