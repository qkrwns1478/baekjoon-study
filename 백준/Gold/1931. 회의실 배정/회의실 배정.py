import sys
input = sys.stdin.readline

n = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(n))
arr.sort(key=lambda x: (x[1], x[0]))
#print(arr)

answer = 0
end = -1
for i in range(n):
    s, e = arr[i]
    if s >= end:
        end = e
        answer += 1
print(answer)