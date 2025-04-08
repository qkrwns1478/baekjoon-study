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

arr = list(map(int, input().split()))
for i in range(start_idx+1, start_idx+n+1):
    tree[i] = arr[i-start_idx-1]

def create_tree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

create_tree(size-1)

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

for _ in range(m):
    a, b = map(int, input().split())
    a += start_idx
    b += start_idx
    print(get_sum(a, b))