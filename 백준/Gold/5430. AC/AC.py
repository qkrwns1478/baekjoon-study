from collections import deque
from sys import stdin
input = stdin.readline

def delete(arr, mode):
    if len(arr) == 0:
        return False
    if not mode:
        arr.popleft()
    else:
        arr.pop()
    return True

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    s = input().strip()
    if s == '[]':
        x = deque()
    else:
        x = deque(map(int, s[1:-1].split(',')))
    is_reversed = False
    is_valid = True
    for c in p:
        if c == "R":
            is_reversed = not is_reversed
        else:
            res = delete(x, is_reversed)
            if not res:
                is_valid = False
                break
    if not is_valid:
        print('error')
        continue

    n = len(x)
    print('[', end='')
    rng = range(0, n) if not is_reversed else range(n-1, -1, -1)
    for i in rng:
        print(x[i], end='')
        if (not is_reversed and i != n-1) or (is_reversed and i != 0):
            print(',', end='')
    print(']')
