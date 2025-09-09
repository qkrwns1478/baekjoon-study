import sys
input = sys.stdin.readline

def verify_board(x, y):
    cntB = 0
    cntW = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0 and arr[x+i][y+j] != 'B':
                cntB += 1
            elif i % 2 == 0 and j % 2 == 1 and arr[x+i][y+j] != 'W':
                cntB += 1
            elif i % 2 == 1 and j % 2 == 0 and arr[x+i][y+j] != 'W':
                cntB += 1
            elif i % 2 == 1 and j % 2 == 1 and arr[x+i][y+j] != 'B':
                cntB += 1
            if i % 2 == 0 and j % 2 == 0 and arr[x+i][y+j] != 'W':
                cntW += 1
            elif i % 2 == 0 and j % 2 == 1 and arr[x+i][y+j] != 'B':
                cntW += 1
            elif i % 2 == 1 and j % 2 == 0 and arr[x+i][y+j] != 'B':
                cntW += 1
            elif i % 2 == 1 and j % 2 == 1 and arr[x+i][y+j] != 'W':
                cntW += 1
    return min(cntB, cntW)

n, m = map(int, input().split())
arr = [[None] * m for _ in range(n)]
for i in range(n):
    s = input().strip()
    for j in range(m):
        arr[i][j] = s[j]

ans = float('inf')
for i in range(n-8+1):
    for j in range(m-8+1):
        ans = min(ans, verify_board(i, j))
print(ans)