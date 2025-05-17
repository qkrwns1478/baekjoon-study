#include <stdio.h>
#include <stdlib.h>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
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

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);

    for (int i = 0; i < k; i++) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        int sx = MIN(a, c);
        int ex = MAX(a, c);
        int sy = MIN(b, d);
        int ey = MAX(b, d);
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

    qsort(sizes, count, sizeof(int), compare);

    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf("%d ", sizes[i]);
    }
    printf("\n");

    return 0;
}