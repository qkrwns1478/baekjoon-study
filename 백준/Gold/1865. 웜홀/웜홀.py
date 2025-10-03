tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = list()
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    def bellman():
        d = [0] * (n+1)
        for i in range(n):
            for s, e, t in edges:
                if d[e] > d[s] + t:
                    d[e] = d[s] + t
                    if i == n-1:
                        return True
        return False

    print("YES" if bellman() else "NO")