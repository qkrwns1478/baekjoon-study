from collections import defaultdict
a, b, c = map(int, input().split())
D = defaultdict(int)
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        D[i] += 1
answer = 0
for i in D:
    if D[i] == 3: answer += c * 3
    elif D[i] == 2: answer += b * 2
    elif D[i] == 1: answer += a
print(answer)