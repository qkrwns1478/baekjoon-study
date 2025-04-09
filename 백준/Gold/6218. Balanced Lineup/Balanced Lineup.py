import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = 0
length = n
while length > 0:
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

def create_tree(i):
    while i != 1:
        if tree_max[i//2] < tree_max[i]:
            tree_max[i//2] = tree_max[i]
        if tree_min[i//2] > tree_min[i]:
            tree_min[i//2] = tree_min[i]
        i -= 1

create_tree(size-1)

def calc(s, e):
    result_max = 0
    result_min = float("inf")
    while s <= e:
        if s % 2 == 1:
            result_max = max(tree_max[s], result_max)
            result_min = min(tree_min[s], result_min)
            s += 1
        if e % 2 == 0:
            result_max = max(tree_max[e], result_max)
            result_min = min(tree_min[e], result_min)
            e -= 1
        s //= 2
        e //= 2
    return result_max - result_min

for _ in range(m):
    a, b = map(int, input().split())
    a += start_idx
    b += start_idx
    print(calc(a, b))