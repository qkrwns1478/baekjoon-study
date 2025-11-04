class Node:
    def __init__(self, value):
        self.value = value
        self.child = dict()
    def add_child(self, child):
        self.child[child.value] = child

n, m = map(int, input().split())
d = dict()
for _ in range(n):
    s = input()
    c = s[0]
    if c not in d:
        d[c] = Node(c)
    cur = d[c]
    for i in range(1, len(s)):
        c = s[i]
        if c not in cur.child:
            cur.add_child(Node(c))
        cur = cur.child[c]

answer = 0
for _ in range(m):
    s = input()
    c = s[0]
    if c not in d:
        continue
    flag = True
    cur = d[c]
    for i in range(1, len(s)):
        c = s[i]
        if c not in cur.child:
            flag = False
            break
        cur = cur.child[c]
    if flag:
        answer += 1

print(answer)