#include <iostream>

using namespace std;
int main() {
    double w, h;
    cin >> w;
    cin >> h;
    double bmi = w / (h*h);
    if (bmi > 25) cout << "Overweight" << endl;
    else if(bmi < 18.5) cout << "Underweight" << endl;
    else cout << "Normal weight" << endl;

    return 0;
}