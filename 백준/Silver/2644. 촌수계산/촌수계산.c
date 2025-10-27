#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

typedef struct Queue {
    Node *front;
    Node *rear;
    int len;
} Queue;

void initQueue(Queue *q) {
    q->front = NULL;
    q->rear = NULL;
    q->len = 0;
}

int isEmpty(Queue *q) {
    return q->len == 0;
}

void enqueue(Queue *q, int val) {
    Node *tmp = (Node *)malloc(sizeof(Node));
    tmp->value = val;
    tmp->next = NULL;
    if (isEmpty(q)) {
        q->front = tmp;
        q->rear = tmp;
    } else {
        q->rear->next = tmp;
        q->rear = tmp;
    }
    q->len++;
}

int dequeue(Queue *q) {
    Node *tmp = q->front;
    int res = tmp->value;
    q->front = tmp->next;
    if (q->front == NULL)
        q->rear = NULL;
    free(tmp);
    q->len--;
    return res;
}

int main() {
    int n;
    scanf("%d", &n);

    int **arr = (int **)calloc(n+1, sizeof(int *));
    for (int i = 0; i < n+1; i++) {
        arr[i] = (int *)calloc(n+1, sizeof(int));
    }

    int a, b;
    scanf("%d %d", &a, &b);

    int m;
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        arr[x][y] = 1;
        arr[y][x] = 1;
    }

    int answer = -1;
    Queue *q = (Queue *)malloc(sizeof(Queue));
    initQueue(q);
    enqueue(q, a);
    int *visited = (int *)calloc(n+1, sizeof(int));
    for (int i = 0; i < n+1; i++)
        visited[i] = -1;
    visited[a] = 0;

    while (!isEmpty(q)) {
        int cur = dequeue(q);
        if (cur == b) {
            answer = visited[b];
            break;
        }
        for (int i = 1; i < n+1; i++) {
            if (arr[cur][i] == 1 && visited[i] == -1) {
                visited[i] = visited[cur] + 1;
                enqueue(q, i);
            }
        }
    }

    printf("%d\n", answer);

    while (!isEmpty(q)) {
        dequeue(q);
    }
    free(q);
    for (int i = 0; i < n+1; i++) {
        free(arr[i]);
    }
    free(arr);
    free(visited);
    return 0;
}