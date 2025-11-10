#include<iostream>
using namespace std;

int main(int argc, char** argv) {
	for (int t = 1; t <= 10; t++) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        int answer = 0;
        for (int i = 2; i < n-2; i++) {
            int maxLeft = max(arr[i-2], arr[i-1]);
            int maxRight = max(arr[i+1], arr[i+2]);
            if (arr[i] > maxLeft && arr[i] > maxRight)
                answer += arr[i] - max(maxLeft, maxRight);
        }
        cout << "#" << t << " " << answer << endl;
	}
	return 0;
}