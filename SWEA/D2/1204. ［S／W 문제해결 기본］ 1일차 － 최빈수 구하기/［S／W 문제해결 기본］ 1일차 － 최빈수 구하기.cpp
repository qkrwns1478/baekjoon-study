#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case){
        int t;
        cin >> t;
        vector<int> arr(1000);
       for (int i=0; i<1000; i++)
           cin >> arr[i];
        sort(arr.begin(), arr.end());
        int prev = -1;
        int maxVal = -1;
        int maxCnt = 0;
        for (int i=0; i<1000; i++) {
        	if (arr[i] != prev) {
            	prev = arr[i];
                int tmp = count(arr.begin(), arr.end(), arr[i]);
                if (tmp >= maxCnt) {
                	maxCnt = tmp;
                    maxVal = arr[i];
                }
            }
        }
        cout << "#" << t << " " << maxVal << endl;
	}
	return 0;
}