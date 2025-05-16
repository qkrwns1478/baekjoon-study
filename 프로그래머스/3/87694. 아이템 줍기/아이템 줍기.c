#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))

typedef struct Node {
    int dist;
    int x;
    int y;
    struct Node *next;
} Node;

typedef struct Queue {
    Node *front;
    Node *rear;
    int count;
} Queue;

void init_queue(Queue *queue);
bool is_empty(Queue *queue);
void enqueue(Queue *queue, int d, int x, int y);
int* dequeue(Queue *queue);

int solution(int **rect, size_t r, size_t c, int characterX, int characterY, int itemX, int itemY) {
    int arr[102][102] = {0};
    for (int i = 0; i < r; i++) {
        int a = rect[i][0] * 2;
        int b = rect[i][1] * 2;
        int c = rect[i][2] * 2;
        int d = rect[i][3] * 2;
        int ax = MIN(a, c);
        int bx = MAX(a, c);
        int ay = MIN(b, d);
        int by = MAX(b, d);
        for (int x = ax; x <= bx; x++) {
            for (int y = ay; y <= by; y++) {
                arr[x][y] = 1;
            }
        }
    }
    for (int i = 0; i < r; i++) {
        int x1 = rect[i][0] * 2;
        int y1 = rect[i][1] * 2;
        int x2 = rect[i][2] * 2;
        int y2 = rect[i][3] * 2;

        int ax = MIN(x1, x2);
        int bx = MAX(x1, x2);
        int ay = MIN(y1, y2);
        int by = MAX(y1, y2);

        for (int x = ax + 1; x < bx; x++) {
            for (int y = ay + 1; y < by; y++) {
                arr[x][y] = 0;
            }
        }
    }

    characterX *= 2;
    characterY *= 2;
    itemX *= 2;
    itemY *= 2;

    int visited[102][102] = {0};
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    Queue queue;
    init_queue(&queue);
    enqueue(&queue, 0, characterX, characterY);
    visited[characterX][characterY] = 1;
    while (!is_empty(&queue)) {
        int *data = dequeue(&queue);
        int d = data[0];
        int x = data[1];
        int y = data[2];
        if (x == itemX && y == itemY) {
            return d / 2;
        }
        
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (1 <= nx && nx < 102 && 1 <= ny && ny < 102) {
                if (visited[nx][ny] == 0 && arr[nx][ny] == 1) {
                    visited[nx][ny] = 1;
                    enqueue(&queue, d+1, nx, ny);
                }
            }
        }
    }
}

void init_queue(Queue *queue) {
    queue->front = NULL;
    queue->rear = NULL;
    queue->count = 0;
}

bool is_empty(Queue *queue) {
    return queue->count == 0;
}

void enqueue(Queue *queue, int d, int x, int y) {
    Node *new = (Node *) malloc(sizeof(Node));
    new->dist = d;
    new->x = x;
    new->y = y;
    new->next = NULL;
    
    if (is_empty(queue))
        queue->front= new;
    else
        queue->rear->next = new;
    
    queue->rear = new;
    queue->count++;
}

int* dequeue(Queue *queue) {
    static int res[3] = {0, 0, 0};
    Node *now;
    if (is_empty(queue))
        return res;
    res[0] = queue->front->dist;
    res[1] = queue->front->x;
    res[2] = queue->front->y;
    now = queue->front;
    queue->front = now->next;
    free(now);
    queue->count--;
    return res;
}