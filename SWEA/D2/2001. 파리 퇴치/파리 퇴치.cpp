#include<iostream>
#include<vector>
using namespace std;

int getSum(vector<vector<int>> &A, int sx, int ex, int sy, int ey) {
	int res = 0;
    for (int i = sx; i <= ex; i++) {
    	for (int j = sy; j <= ey; j++) {
        	res += A[i][j];
        }
    }
    return res;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N, M;
        cin >> N >> M;
        vector<vector<int>> arr(N, vector<int>(N));
        for (int i=0; i<N; i++) {
        	for (int j=0; j<N; j++) {
            	cin >> arr[i][j];
            }
        }
        /* vector<vector<int>> prev;
        vector<vector<int>> cur = arr;
        int size;
        for (int m=2; m<=M; m++) {
            size = N - (m-1);
            prev = cur;
        	cur = vector<vector<int>>(size, vector<int>(size));
            for (int i=0; i<size; i++) {
            	for (int j=0; j<size; j++) {
                    cur[i][j] = prev[i][j] + prev[i+1][j] + prev[i][j+1] + prev[i+1][j+1];
                }
            }
        } */
        int size = N - (M-1);
        int maxVal = 0;
        int cur;
        for (int i=0; i<size; i++) {
        	for (int j=0; j<size; j++) {
            	cur = getSum(arr, i, i+(M-1), j, j+(M-1));
                maxVal = max(maxVal, cur);
        	}
        }
        cout << "#" << test_case << " " << maxVal << endl;
	}
	return 0;
}