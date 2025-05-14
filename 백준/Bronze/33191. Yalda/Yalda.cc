#include <iostream>
using namespace std;
int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    if (a >= b) cout << "Watermelon\n";
    else if (a >= c) cout << "Pomegranates\n";
    else if (a >= d) cout << "Nuts\n";
    else cout << "Nothing\n";
    return 0;
}