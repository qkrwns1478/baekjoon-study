root = list()

def find(x):
    if x == root[x]:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(A, B):
    rootA = find(A)
    rootB = find(B)
    if rootA == rootB:
        return False
    root[rootA] = rootB;
    return True

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = list()
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append([n1, n2, w])
    edges.sort(key=lambda x: x[2])

    root = list(i for i in range(V+1))

    answer = 0
    cnt = 0
    for A, B, W in edges:
        if union(A, B):
            answer += W
            cnt += 1
            if cnt == V:
                break
    print(f"#{t} {answer}")
