from collections import deque

def divide(n):
    if n % 2 == 0:
        return [n // 2]
    else:
        return [(n-1) // 2, (n-1) // 2 + 1]

N, M = map(int, input().split())

def bfs(N):
    queue = deque([N])
    visited = set()
    while queue:
        cur = queue.popleft()
        if cur == M:
            return True
        hearts = divide(cur)
        for h in hearts:
            if h == M:
                return True
            elif h not in visited:
                visited.add(h)
                queue.append(h)
    return False

print("YES" if bfs(N) else "NO")
