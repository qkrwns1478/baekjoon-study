from collections import deque
n = int(input())
arr = list(map(int, input().split()))
cards = deque()

idx = 1
while arr:
    i = arr.pop()
    if i == 1: cards.appendleft(idx)
    elif i == 2: cards.insert(1, idx)
    else: cards.append(idx)
    idx += 1

print(*cards)