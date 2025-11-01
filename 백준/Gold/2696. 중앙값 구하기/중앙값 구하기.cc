#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Heapq {
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    public:
    void addNum(int num) {
        // 새로 들어온 숫자를 최대 힙에 넣음
        maxHeap.push(num);
        // 힙 균형 맞추기
        if (!maxHeap.empty() && !minHeap.empty()) {
            if (maxHeap.top() > minHeap.top()) {
                int val = maxHeap.top();
                maxHeap.pop();
                minHeap.push(val);
            }
        }
        // 힙들의 크기 균형 맞추기
        if (maxHeap.size() > minHeap.size() + 1) {
            int val = maxHeap.top();
            maxHeap.pop();
            minHeap.push(val);
        }
        if (minHeap.size() > maxHeap.size()) {
            int val = minHeap.top();
            minHeap.pop();
            maxHeap.push(val);
        }
    }

    int getMedian() {
        return maxHeap.top();
    }
};

vector<int> getArray(int m) {
    int n = (m + 9) / 10;
    vector<int> arr;
    for (int i = 0; i < n; i++) {
        int cnt = min(10, m - (int)arr.size());
        for (int j = 0; j < cnt; j++) {
            int tmp;
            cin >> tmp;
            arr.push_back(tmp);
        }
    }
    return arr;
}

void printArray(const vector<int> &arr) {
    int n = arr.size();
    cout << n << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i];
        if ((i + 1) % 10 == 0 || i == n - 1) {
            cout << endl;
        } else {
            cout << " ";
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int m;
        cin >> m;
        vector<int> arr = getArray(m);
        vector<int> res;
        Heapq hq;
        for (int i = 0; i < m; i++) {
            hq.addNum(arr[i]);
            if ((i+1) % 2 == 1) {
                res.push_back(hq.getMedian());
            }
        }
        printArray(res);
    }
    return 0;
}