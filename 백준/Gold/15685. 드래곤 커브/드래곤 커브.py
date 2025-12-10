dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dragon_curve(n):
    if n == 0:
        return [0]
    prev = dragon_curve(n-1)
    tf = [(d+1) % 4 for d in prev[::-1]]
    return prev + tf

N = int(input())
dragon = set()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon.add((x, y))
    dcs = dragon_curve(g)
    for dc in dcs:
        cd = (d + dc) % 4
        x += dx[cd]
        y += dy[cd]
        dragon.add((x, y))

answer = 0
for x, y in dragon:
    if (x, y+1) in dragon and (x+1, y) in dragon and (x+1, y+1) in dragon:
        answer += 1
print(answer)
