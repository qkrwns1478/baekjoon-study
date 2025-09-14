class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = dict()
        self.is_leaf = False
    def add_child(self, key, child):
        self.child[key] = child
    def find_child(self, key):
        return self.child.get(key)

t = int(input())
for _ in range(t):
    n = int(input())
    root = Node('', None)
    flag = True
    arr = list()
    for _ in range(n):
        arr.append(input())
    arr.sort(key=lambda x: (x, -len(x)))
    for s in arr:
        cur = root
        for i in range(len(s)):
            ch = cur.find_child(s[i])
            if not ch:
                ch = Node(s[i], cur)
            if cur.is_leaf:
                flag = False
                break
            cur.add_child(s[i], ch)
            cur = ch
        if not flag:
            break
        cur.is_leaf = True
    print("YES" if flag else "NO")