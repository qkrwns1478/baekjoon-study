#include<iostream>
using namespace std;

int main(int argc, char** argv){
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case){
        int x;
        cin >> x;
        if (x == 1) {
            cout << 0 << endl;
            continue;
        }
        int A = x / 2;
        int B = x % 2;
        string s = "";
        if (B == 1) s += "4";
        for (int i=0; i<A; i++) s += "8";
        cout << s << endl;
	}
	return 0;
}