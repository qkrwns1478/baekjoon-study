#include <iostream>
#include <iomanip>

using namespace std;
int main() {
    int d1, d2;
    const double PI = 3.141592;
    cin >> d1;
    cin >> d2;
    double answer = 2 * PI * d2 + 2 * d1;
    cout << std::setprecision(6) << std::fixed << answer << endl;

    return 0;
}