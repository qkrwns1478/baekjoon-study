from collections import deque

C = int(input())
for c in range(1, C+1):
    N, M = map(int, input().split())
    L = len(str(N))

    def bfs(n, m):
        queue = deque()
        queue.append((n, 0))
        visited = set()
        visited.add((n, 0))
        answer = -1

        while queue:
            cur_n, cur_m = queue.popleft()
            if cur_m == m:
                answer = max(answer, cur_n)
                continue
            arr = list(str(cur_n))
            for i in range(L-1):
                for j in range(i+1, L):
                    if i == 0 and arr[j] == '0':
                        continue
                    arr[i], arr[j] = arr[j], arr[i]
                    nxt = int(''.join(arr))
                    if (nxt, cur_m + 1) not in visited:
                        queue.append((nxt, cur_m + 1))
                        visited.add((nxt, cur_m + 1))
                    arr[i], arr[j] = arr[j], arr[i]
        return answer

    print(f"#{c} {bfs(N, M)}")
