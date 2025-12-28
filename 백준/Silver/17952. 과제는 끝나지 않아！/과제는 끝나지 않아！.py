N = int(input())
stack = list()
score = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        a = arr[1]
        t = arr[2]
    else:
        if not stack:
            continue
        a, t = stack.pop()
    if t == 1:
        score += a
    else:
        stack.append((a, t-1))

print(score)