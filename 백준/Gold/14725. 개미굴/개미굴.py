class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = list()
    def add_child(self, child):
        self.child.append(child)
        self.child.sort(key=lambda x:(x.value), reverse=True)
    def find_child(self, key):
        for ch in self.child:
            if ch.value == key:
                return ch
        return None

n = int(input())
root = Node('', None)

for _ in range(n):
    s = list(input().split())
    cur = root
    for i in range(1, len(s)):
        ch = cur.find_child(s[i])
        if not ch:
            ch = Node(s[i], cur)
            cur.add_child(ch)
        cur = ch

stack = list()
stack.append((root, 0))
while stack:
    cur, level = stack.pop()
    if level > 0:
        print("--" * (level-1) + cur.value)
    for ch in cur.child:
        stack.append((ch, level+1))