import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    #for i in range(1, v+1):
    #    print(f"{i} : {adj[i]}")
    
    def dfs(i, mode):
        visited[i] = mode
        for j in adj[i]:
            if visited[j] == -1:
                dfs(j, (mode+1)%2)
        '''print(visited[1:])
        for j in adj[i]:
            print(f"{i} ({visited[i]}) - {j} ({visited[j]})")
           if visited[i] == visited[j]:
                return False
        return True'''
        
    visited = [-1] * (v+1)
    for i in range(1, v+1):
        if visited[i] == -1:
            dfs(i, 0)

    flag = True
    for i in range(1, v+1):
        for j in adj[i]:
            if visited[i] == visited[j]:
                flag = False
                break
    
    print("YES" if flag else "NO")