#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() {
    int n;
    scanf("%d", &n);

    int **map = (int **)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; i++) {
        map[i] = (int *)malloc(sizeof(int) * 2);
        scanf("%d %d", &map[i][0], &map[i][1]);
    }

    double answer = 0;
    for (int i = 0; i < n; i++) {
        answer += (long long)map[i][0] * map[(i+1)%n][1] - (long long)map[(i+1)%n][0] * map[i][1];
    }
    printf("%.1f\n", fabs(answer) / 2.0);

    for (int i = 0; i < n; i++) {
        free(map[i]);
    }
    free(map);
    return 0;
}