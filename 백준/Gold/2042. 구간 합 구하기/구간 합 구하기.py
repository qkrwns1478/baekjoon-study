n, m, k = map(int, input().split())
t = 0
length = n
while length >= 1:
    length //= 2
    t += 1

size = 2**t * 2
start_idx = 2**t - 1
tree = [0] * (size+1)

for i in range(start_idx+1, start_idx+n+1):
    tree[i] = int(input())

i = size - 1
while i > 1:
    tree[i//2] += tree[i]
    i -= 1

def get_sum(s, e):
    result = 0
    while s <= e:
        if s%2 == 1:
            result += tree[s]
            s += 1
        if e%2 == 0:
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

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        modify(start_idx + b, c)
    else:
        print(get_sum(start_idx + b, start_idx + c))