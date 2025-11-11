n = int(input())
words = set()
for _ in range(n):
    words.add(input())
input() # 빈줄 입력 처리

class Node:
    def __init__(self, value):
        self.value = value
        self.child = dict()
        self.is_end = False
    def add_child(self, child):
        self.child[child.value] = child

root = Node('')
for w in words:
    cur = root
    for c in w:
        if c not in cur.child:
            cur.add_child(Node(c))
        cur = cur.child[c]
    cur.is_end = True

def get_score(l):
    if l <= 2:
        return 0
    elif l <= 4:
        return 1
    elif l == 5:
        return 2
    elif l == 6:
        return 3
    elif l == 7:
        return 5
    else:
        return 11     

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

b = int(input())
for b_idx in range(b):
    arr = [list(input()) for _ in range(4)]
    visited = [[False] * 4 for _ in range(4)]
    res = set()

    def dfs(x, y, node, cur):
        global res
        if node.is_end:
            res.add(cur)
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                nc = arr[nx][ny]
                if nc in node.child:
                    dfs(nx, ny, node.child[nc], cur + nc)
        visited[x][y] = False

    for i in range(4):
        for j in range(4):
            c = arr[i][j]
            if c in root.child:
                dfs(i, j, root.child[c], c)

    score = 0
    max_length = 0
    max_s = ''
    for s in res:
        l = len(s)
        score += get_score(l)
        if l > max_length:
            max_length = l
            max_s = s
        elif l == max_length:
            max_s = min(max_s, s)  
    print(score, max_s, len(res))
    if b_idx != b-1:
        input() # 빈줄 입력 처리