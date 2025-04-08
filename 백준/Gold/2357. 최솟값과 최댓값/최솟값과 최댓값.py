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
tree_max = [0] * (size+1)
tree_min = [float("inf")] * (size+1)

for i in range(start_idx+1, start_idx+n+1):
    p = int(input())
    tree_max[i] = p
    tree_min[i] = p

def createTree(i):
    while i != 1:
        if tree_max[i//2] < tree_max[i]:
            tree_max[i//2] = tree_max[i]
        if tree_min[i//2] > tree_min[i]:
            tree_min[i//2] = tree_min[i]
        i -= 1

createTree(size-1)

def get_max(s, e):
    result = 0
    while s <= e:
        if s % 2 == 1:
            result = max(tree_max[s], result)
            s += 1
        if e % 2 == 0:
            result = max(tree_max[e], result)
            e -= 1
        s //= 2
        e //= 2
    return result

def get_min(s, e):
    result = float("inf")
    while s <= e:
        if s % 2 == 1:
            result = min(tree_min[s], result)
            s += 1
        if e % 2 == 0:
            result = min(tree_min[e], result)
            e -= 1
        s //= 2
        e //= 2
    return result

for _ in range(m):
    a, b = map(int, input().split())
    a += start_idx
    b += start_idx
    print(get_min(a, b), get_max(a, b))