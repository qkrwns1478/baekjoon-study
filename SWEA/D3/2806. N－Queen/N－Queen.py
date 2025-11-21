dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

T = int(input())
for t in range(1, T+1):
    N = int(input())

    def get_queen_range(x, y, arr, flag=True):
        for i in range(8):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    arr[nx][ny] += 1 if flag else -1
                else:
                    break

    def solution(x, y, arr):
        res = 0
        get_queen_range(x, y, arr)
        if arr[x][y] > 0:
            get_queen_range(x, y, arr, False)
            return 0
        if y == N-1 and arr[x][y] == 0:
            get_queen_range(x, y, arr, False)
            return 1
        for i in range(N):
            res += solution(i, y+1, arr)
        get_queen_range(x, y, arr, False)
        return res

    ans = 0
    for i in range(N):
        arr = [[0] * N for _ in range(N)]
        ans += solution(i, 0, arr)
    print(f"#{t} {ans}")