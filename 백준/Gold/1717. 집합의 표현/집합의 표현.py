def init(x):
    global D
    if x not in D:
        D[x] = x
        nums[x] = 0

def find(x):
    global D
    if D[x] == x:
        return x
    D[x] = find(D[x])
    return D[x]

def union(a, b):
    global D
    global nums
    A, B = find(a), find(b)
    if A != B:
        if nums[A] < nums[B]:
            D[A] = B
        elif nums[A] > nums[B]:
            D[B] = A
        else:
            D[B] = A
            nums[A] += 1

n, m = map(int, input().split())
D = dict()
nums = dict()
for _ in range(m):
    q, a, b = map(int, input().split())
    init(a)
    init(b)
    if q == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")