import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = list()
    def add_child(self, child):
        self.child.append(child)
    def remove_child(self, child):
        if child in self.child:
            self.child.remove(child)

class Tree:
    def __init__(self, root: Node):
        self.root = root

n = int(input())
root = Node("root", None)
tree = Tree(root)

for _ in range(n):
    st = "root\\" + input().strip()
    arr = list(st.split('\\'))
    for i in range(1, len(arr)):
        cur = tree.root
        for j in range(1, i+1):
            flag = False
            for ch in cur.child:
                if ch.value == arr[j]:
                    flag = True
                    cur = ch
                    break
            if not flag:
                new_node = Node(arr[j], cur)
                cur.add_child(new_node)
                cur = new_node

stack = list()
stack.append((tree.root, 0))
while stack:
    cur, level = stack.pop()
    if level > 0:
        print(' ' * (level-1) + cur.value)
    cur.child.sort(key=lambda x:(x.value), reverse=True)
    for ch in cur.child:
        stack.append((ch, level+1))