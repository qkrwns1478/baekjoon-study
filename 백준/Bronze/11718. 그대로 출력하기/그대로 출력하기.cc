#include <iostream>
using namespace std;

int main(){
    string s;
    
    while(1==1){
        getline(cin >> ws, s);
        if(cin.eof()) break;
        cout << s << endl;
    }

    return 0;
}