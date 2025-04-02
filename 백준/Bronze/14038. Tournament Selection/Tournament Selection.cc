#include <iostream>

using namespace std;
int main() {
    int w = 0;
    char input;
    for (int i=0; i<6; i++){
        cin >> input;
        if(input == 'W') w++;
    }
    int answer = -1;
    if (w==5 || w==6)answer = 1;
    else if (w==3 || w==4) answer = 2;
    else if (w==1 || w==2) answer = 3;
    cout << answer << endl;

    return 0;
}