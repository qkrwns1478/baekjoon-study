from collections import deque

def get_max(q):
    if not q:
        return 0
    return max(list(q))

T = int(input())
for t in range(1, T+1):
    n = int(input())
    q = deque(map(int, input().split()))
    max_val = get_max(q)
    profit, loss, stock = 0, 0, 0
    while q:
        cur = q.popleft()
        if cur == max_val:
            profit += cur * stock - loss
            max_val = get_max(q)
            loss, stock = 0, 0
        else:
            loss += cur
            stock += 1
    print(f"#{t} {profit}")