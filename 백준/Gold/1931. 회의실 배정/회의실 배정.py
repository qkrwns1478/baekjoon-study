import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 2 for _ in range(n)]
for i in range(n):
    s, e = map(int, input().split())
    arr[i][1] = s
    arr[i][0] = e

arr.sort()
answer = 0
end = -1

for i in range(n):
    if arr[i][1] >= end:
        end = arr[i][0]
        answer += 1

print(answer)