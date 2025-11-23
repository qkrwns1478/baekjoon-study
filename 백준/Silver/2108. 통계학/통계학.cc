#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int average(vector<int> arr, int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    sum /= static_cast<double>(n);
    return static_cast<int>(round(sum));
}

int median(vector<int> arr, int n) {
    sort(arr.begin(), arr.end());
    return arr[n/2];
}

int mode(vector<int> arr, int n) {
    map<int, int> tmp;
    for (int i = 0; i < n; i++) {
        tmp[arr[i]]++;
    }
    int maxVal = -4000;
    for (const auto& pair : tmp) {
        if (maxVal < pair.second)
            maxVal = pair.second;
    }
    vector<int> tmpArr;
    for (const auto& pair : tmp) {
        if (pair.second == maxVal)
            tmpArr.push_back(pair.first);
    }
    if (tmpArr.size() == 1) {
        return tmpArr[0];
    } else {
        sort(tmpArr.begin(), tmpArr.end());
        return tmpArr[1];
    }
}

int range(vector<int> arr, int n) {
    int maxVal = -4000;
    int minVal = 4000;
    for (int i = 0; i < n; i++) {
        if (arr[i] < minVal)
            minVal = arr[i];
        if (arr[i] > maxVal)
            maxVal = arr[i];
    }
    return maxVal - minVal;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << average(arr, n) << endl;
    cout << median(arr, n) << endl;
    cout << mode(arr, n) << endl;
    cout << range(arr, n) << endl;
    return 0;
}