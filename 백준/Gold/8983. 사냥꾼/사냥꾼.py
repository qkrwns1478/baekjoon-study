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
#print(sade)
#print(animals)

hunted = [False] * n
answer = 0
for x in sade:
    for i in range(n):
        a, b = animals[i][0], animals[i][1]
        if abs(x-a) + b <= l and not hunted[i]:
            answer += 1
            hunted[i] = True

print(answer)