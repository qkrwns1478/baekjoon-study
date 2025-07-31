#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x;
    cin >> x;
    if (0 <= x && x <= pow(10, 100))
        cout << "FA" << endl;
    else
        cout << "NFA" << endl;
    return 0;
}