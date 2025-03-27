import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self, node):
        if node is not None:
            print(node.key, end="")
            if node.left:
                self.pre_order(node.left)
            if node.right:
                self.pre_order(node.right)

    def in_order(self, node):
        if node is not None:
            if node.left:
                self.in_order(node.left)
            print(node.key, end="")
            if node.right:
                self.in_order(node.right)

    def post_order(self, node):
        if node is not None:
            if node.left:
                self.post_order(node.left)
            if node.right:
                self.post_order(node.right)
            print(node.key, end="")

n = int(input())
nodes = [None] * n
for i in range(n):
    nodes[i] = Node(chr(i+65))

tree = Tree()
tree.root = nodes[0]

for _ in range(n):
    p, l, r = input().split()
    np = nodes[ord(p)-65]
    if l != ".":
        nl = nodes[ord(l)-65]
        np.left = nl
    if r != ".":
        nr = nodes[ord(r)-65]
        np.right = nr

tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
print()
tree.post_order(tree.root)
print()