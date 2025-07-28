#include <stdio.h>
#include <stdlib.h>
int dfs(int x, int y, char** arr, int** visited, int n, int m) {
  visited[x][y] = 1;
  int res = 1;
  int dx[4] = {1, -1, 0, 0};
  int dy[4] = {0, 0, 1, -1};
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (0 <= nx && nx < n && 0 <= ny && ny < m) {
      if (visited[nx][ny] != 1 && arr[nx][ny] == arr[x][y])
        res += dfs(nx, ny, arr, visited, n, m);
    }
  }
  return res;
}
int main() {
  int n, m;
  scanf("%d %d", &m, &n);
  char **arr = (char **)malloc(sizeof(char*) * n);
  int **visited = (int **)malloc(sizeof(int*) * n);
  for (int i = 0; i < n; i++) {
    arr[i] = (char *)malloc(sizeof(char) * m);
    visited[i] = (int *)malloc(sizeof(int) * m);
    char tmp[100];
    scanf("%s", tmp);
    for (int j = 0; j < m; j++) {
      arr[i][j] = tmp[j];
    }
  }
  int B = 0;
  int W = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (visited[i][j] != 1) {
        int t = dfs(i, j, arr, visited, n, m);
        if (arr[i][j] == 'B') B += t * t;
        else W += t * t;
      }
    }
  }
  printf("%d %d\n", W, B);
  for (int i = 0; i < n; i++) {
    free(arr[i]);
    free(visited[i]);
  }
  free(arr);
  free(visited);
  return 0;
}