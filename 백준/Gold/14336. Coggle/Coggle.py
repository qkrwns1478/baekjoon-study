class Node:
    def __init__(self, value):
        self.value = value
        self.child = dict()
        self.is_end = False
    def add_child(self, child):
        self.child[child.value] = child

file = open('dict.txt', 'r')
lines = file.readlines()
words = tuple(line.strip() for line in lines)

root = Node('')
for w in words:
    cur = root
    for c in w:
        if c not in cur.child:
            cur.add_child(Node(c))
        cur = cur.child[c]
    cur.is_end = True

arr = [list(input().split()) for _ in range(5)]
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

visited = [[False] * 5 for _ in range(5)]
res = set()

def dfs(x, y, node, cur):
    global res
    if node.is_end:
        res.add(cur)
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            nc = arr[nx][ny]
            if nc in node.child:
                dfs(nx, ny, node.child[nc], cur + nc)
    visited[x][y] = False

for i in range(5):
    for j in range(5):
        c = arr[i][j]
        if c in root.child:
            dfs(i, j, root.child[c], c)

print(len(res))