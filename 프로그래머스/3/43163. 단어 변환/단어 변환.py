from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0))

    while queue:
        cur, res = queue.popleft()
        if cur == target:
            return res
        for w in words:
            cnt = 0
            for i in range(len(cur)):
                if cur[i] != w[i]:
                    cnt += 1
            if cnt == 1:
                queue.append((w, res+1))
    return 0