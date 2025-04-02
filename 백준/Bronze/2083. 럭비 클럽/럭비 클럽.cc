#include <iostream>

using namespace std;
int main() {
    int a, b;
    string name;
    while(1==1){
        cin >> name >> a >> b;
        if(name == "#" && a == 0 && b == 0) break;
        else if(a > 17 || b >= 80){
            cout << name << " Senior\n";
        } else {
            cout << name << " Junior\n";
        }
    }

    return 0;
}