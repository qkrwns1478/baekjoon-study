#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int N;
	cin >> N;
    for (int i = 1; i <= N; i++) {
    	string s = to_string(i);
        for (char &c: s) {
        	if (c == '3' || c == '6' || c == '9')
            	c = '-';
        }
        if (s.find('-') == string::npos)
            cout << i << (i == N ? "\n" : " ");
        else {
        	int cnt = count(s.begin(), s.end(), '-');
            for (int j = 0; j < cnt; j++)
                cout << '-';
            cout << (i == N ? "\n" : " ");
        }
    }
	return 0;
}