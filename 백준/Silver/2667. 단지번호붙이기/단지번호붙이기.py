import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def apt(x, y):
    if visited[x][y]:
        return 0
    
    visited[x][y] = True
    result = 1 if arr[x][y] == 1 else 0

    if arr[x][y] > 0:
        if x > 0 and not visited[x-1][y]:
            result+= apt(x-1, y)
        if x < n-1 and not visited[x+1][y]:
            result += apt(x+1, y)
        if y < n-1 and not visited[x][y+1]:
            result += apt(x, y+1)
        if y > 0 and not visited[x][y-1]:
            result += apt(x, y-1)
            
    return result

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    s = input()
    for j in range(n):
        arr[i][j] = int(s[j])

cnt = 0
answer = []
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] > 0:
            danji = apt(i, j)
            if danji > 0:
                cnt += 1
                answer.append(danji)
            
answer.sort()
print(cnt)
for i in answer:
    print(i)