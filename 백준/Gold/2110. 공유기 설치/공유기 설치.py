import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = list()
for _ in range(n):
    x.append(int(input()))
x.sort()

pl = 1
pr = x[-1] - x[0]
answer = 0

while pl <= pr:
    mid = (pl + pr)//2
    current = x[0]
    cnt = 1

    for i in range(1, n):
        if x[i] - mid >= current:
            cnt += 1
            current = x[i]

    if cnt >= c:
        pl = mid+1
        answer = mid
        
    else:
        pr = mid-1

print(answer)