#include <iostream>
#include <map>
using namespace std;

int main() {
    int x, y;
    map<int, int> dX;
    map<int, int> dY;
    
    for (int i = 0; i < 3; i++) {
        cin >> x >> y;
        dX[x]++;
        dY[y]++;
    }

    for (const auto& pair: dX) {
        if (pair.second == 1) {
            x = pair.first;
            break;
        }
    }
    
    for (const auto& pair: dY) {
        if (pair.second == 1) {
            y = pair.first;
            break;
        }
    }
    cout << x << " " << y << endl;
    return 0;
}