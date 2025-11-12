#include<iostream>
using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;
	cin>>T;
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
	for (test_case = 1; test_case <= T; ++test_case) {
        cout<<"#"<<test_case<<endl;
        int N;
        cin>>N;
        int arr[10][10] = {0,};
        int num = 0;
        int dir = 0;
        int x = 0;
        int y = 0;
        while (num < N*N) {
        	arr[x][y] = ++num;
            bool check = false;
            for (int i=0; i<4; i++) {
            	int curDir = (dir + i) % 4;
                int nx = x + dx[curDir];
                int ny = y + dy[curDir];
                if (0 <= nx && nx < N && 0 <= ny && ny < N && arr[nx][ny] == 0) {
                	check = true;
                    dir = curDir;
                    x = nx;
                    y = ny;
                    break;
                }
            }
            if (check == false) break;
        }
        for (int i=0; i<N; i++) {
        	for (int j=0; j<N-1; j++) {
            	cout << arr[i][j] << " ";
            }
            cout << arr[i][N-1] << endl;
        }
	}
	return 0;
}