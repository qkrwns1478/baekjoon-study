def count(n, a, i): # n, 누적합, 1/2/3
    global cnt
    if a + i == n:
        cnt += 1
        return

    if a + i > n:
        return

    for j in range(1, 4):
        count(n, a+i, j)

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1, 4):
        count(n, 0, i)
    print(cnt)