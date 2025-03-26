import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
sade = list(map(int, input().split()))
animals = list()
for _ in range(n):
    a, b = map(int, input().split())
    animals.append((a,b))

sade.sort()
animals.sort()

answer = 0
for a, b in animals:
    pl = 0
    pr = m-1

    while pl <= pr:
        mid = (pl + pr) // 2
        if a+b-l <= sade[mid] <= a-b+l:
            answer += 1
            break
        elif a+b-l > sade[mid]:
            pl = mid+1
        elif a-b+l < sade[mid]:
            pr = mid-1

print(answer)