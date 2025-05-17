#include <stdio.h>
#include <stdlib.h>

#define LIMIT 100

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int visited[LIMIT][LIMIT] = {0};
int arr[LIMIT][LIMIT] = {0};

int dfs(int y, int x, int m, int n, int arr[][LIMIT]) {
    visited[y][x] = 1;
    int cnt = 1;
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (0 <= ny && ny < m && 0 <= nx && nx < n)
            if (!visited[ny][nx] && arr[ny][nx] == 0)
                cnt += dfs(ny, nx, m, n, arr);
    }
    return cnt;
}

void sort(int *array, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (array[i] > array[j]) {
                int tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }
    }
}

int main() {
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);

    for (int i = 0; i < k; i++) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        int sx = (a < c) ? a : c;
        int ex = (a > c) ? a : c;
        int sy = (b < d) ? b : d;
        int ey = (b > d) ? b : d;
        for (int y = sy; y < ey; y++) {
            for (int x = sx; x < ex; x++) {
                arr[y][x] = 1;
            }
        }
    }

    int sizes[LIMIT * LIMIT] = {0};
    int count = 0;

    for (int y = 0; y < m; y++) {
        for (int x = 0; x < n; x++) {
            if (!arr[y][x] && !visited[y][x]) {
                int area = dfs(y, x, m, n, arr);
                sizes[count++] = area;
            }
        }
    }

    sort(sizes, count);

    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf("%d ", sizes[i]);
    }
    printf("\n");

    return 0;
}