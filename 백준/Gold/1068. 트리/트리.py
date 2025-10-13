class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = set()
        self.is_leaf = True
    def add_child(self, child):
        self.child.add(child)
        self.is_leaf = False
        child.parent = self
    def remove_child(self, child):
        if child in self.child:
            self.child.remove(child)
        if len(self.child) == 0:
            self.is_leaf = True

class Tree:
    def __init__(self, root):
        self.root = root

n = int(input())
nodes = dict()
for i in range(n):
    nodes[i] = Node(i, None)
tree = Tree(None)

arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] == -1:
        tree.root = nodes[i]
    else:
        nodes[arr[i]].add_child(nodes[i])

m = int(input())
if not nodes[m].parent:
    print(0)
else:
    nodes[m].parent.remove_child(nodes[m])
    answer = 0
    def dfs(cur):
        global answer
        if cur.is_leaf:
            answer += 1
            return
        for ch in cur.child:
            dfs(ch)
    dfs(tree.root)
    print(answer)