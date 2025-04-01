#include <iostream>

using namespace std;
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int one = 0;
    int two = 0;
    if(a == 1) one++;
    else two++;
    if(b == 1) one++;
    else two++;
    if(c == 1) one++;
    else two++;
    if(one > two) cout << 1 << endl;
    else cout << 2 << endl;

    return 0;
}