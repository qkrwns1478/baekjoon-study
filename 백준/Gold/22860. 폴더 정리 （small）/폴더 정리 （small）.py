import sys
input = sys.stdin.readline
from collections import defaultdict, deque

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = list()
        self.files = set()
    def add_child(self, child):
        self.child.append(child)
    def remove_child(self, child):
        if child in self.child:
            self.child.remove(child)
    def add_file(self, file):
        self.files.add(file)
    def remove_file(self, file):
        if file in self.files:
            self.files.remove(file)

class Tree:
    def __init__(self, root: Node):
        self.root = root

n, m = map(int, input().strip().split())
root = Node("main", None)
tree = Tree(root)
visited = set()
visited.add("main")

inputs = deque()
for _ in range(n+m):
    inputs.append(input().strip())

while inputs:
    st = inputs.popleft()
    arr = list(st.split())
    if arr[0] not in visited:
        inputs.append(st)
        continue
    visited.add(arr[1])
    if int(arr[2]) == 1: # Folder
        stack = list()
        stack.append(tree.root)
        while True:
            cur = stack.pop()
            if cur.value == arr[0]:
                break
            for c in cur.child:
                stack.append(c)
        child = Node(arr[1], cur)
        cur.add_child(child)
    else: # File
        stack = list()
        stack.append(tree.root)
        while True:
            cur = stack.pop()
            if cur.value == arr[0]:
                break
            for c in cur.child:
                stack.append(c)
        cur.add_file(arr[1])

q = int(input().strip())
for _ in range(q):
    query = list(input().strip().split('/'))
    
    cur = tree.root
    for i in range(1, len(query)):
        for j in range(len(cur.child)):
            if cur.child[j].value == query[i]:
                break
        cur = cur.child[j]

    answer = defaultdict(int)
    for f in cur.files:
        answer[f] += 1
    for ch in cur.child:
        stack = list()
        stack.append(ch)
        while stack:
            curr = stack.pop()
            if curr.files:
                for f in curr.files:
                    answer[f] += 1
            if curr.child:
                for c in curr.child:
                    stack.append(c)

    print(len(answer), sum(answer[i] for i in answer))