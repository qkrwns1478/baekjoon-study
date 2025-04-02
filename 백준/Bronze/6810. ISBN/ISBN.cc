#include <iostream>

using namespace std;
int main() {
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;
    int answer = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3 + a * 1 + b * 3 + c * 1;
    cout << "The 1-3-sum is " << answer << endl;

    return 0;
}