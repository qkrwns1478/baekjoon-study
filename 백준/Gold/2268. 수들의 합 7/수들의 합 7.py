import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = 0
length = n

while length != 0:
    length //= 2
    k += 1

size = 2**k * 2
start_idx = 2**k - 1
tree = [0] * (size+1)

def get_sum(s, e):
    result = 0
    while s <= e:
        if s % 2 == 1:
            result += tree[s]
            s += 1
        if e % 2 == 0:
            result += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return result

def modify(idx, val):
    dv = val - tree[idx]
    while idx > 0:
        tree[idx] += dv
        idx //= 2

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        if b > c:
            b, c = c, b
        b += start_idx
        c += start_idx
        print(get_sum(b, c))
    else:
        modify(start_idx + b, c)