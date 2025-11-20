#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    for (int t=1; t<=T; t++) {
        cout << "#" << t << " ";
        string s;
        cin >> s;
        string yy = s.substr(0, 4);
        string mm = s.substr(4, 2);
        string dd = s.substr(6, 2);
        int yyi = stoi(yy);
        int mmi = stoi(mm);
        int ddi = stoi(dd);
        if (0 < mmi && mmi < 13 && 0< ddi && ddi <= days[mmi])
            cout << yy << "/" << mm << "/" << dd << endl;
        else
            cout << -1 << endl;
    }
    return 0;
}