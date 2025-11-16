#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

void solution(vector<char> &arr, int n, int s) {
    if (n == 0) return;
    int nextSize = pow(3, n-1);
    for (int i = s + nextSize; i < s + nextSize*2; i++) arr[i] = ' ';
    solution(arr, n-1, s);
    solution(arr, n-1, s + nextSize*2);
}

int main() {
    int n;
    while (cin >> n) {
        int size = pow(3, n);
        vector<char> arr(size, '-');
        solution(arr, n, 0);
        for (int i = 0; i < size; i++) cout << arr[i];
        cout << endl;
    }
    return 0;
}