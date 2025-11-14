#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
    	float sum = 0;
        for (int i = 0; i < 10; i++) {
        	int tmp;
            cin >> tmp;
            sum += tmp;
        }
        cout << "#" << t << " " << round(sum / 10) << endl;
    }
	return 0;
}