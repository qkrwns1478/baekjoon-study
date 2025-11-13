from sys import stdin
input = stdin.readline

N = int(input())
A = set(map(int, input().split()))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add_child(self, child):
        if child.value == '1':
            self.right = child
        else:
            self.left = child
    def get_child(self, target):
        if target == '1':
            return self.right
        else:
            return self.left

root = Node('')
n = len(bin(max(A))[2:])
for a in A:
    s = bin(a)[2:].zfill(n)
    cur = root
    for c in s:
        nxt = cur.get_child(c)
        if nxt is None:
            cur.add_child(Node(c))
            nxt = cur.get_child(c)
        cur = nxt

max_xor = 0
for a in A:
    s = bin(a)[2:].zfill(n)
    cur = root
    xor_val = 0
    for c in s:
        x = '0' if c == '1' else '1' # 반대 비트를 선택해서 XOR 최대화
        x_child = cur.get_child(x)
        if x_child is not None:
            xor_val <<= 1
            xor_val |= 1
            cur = x_child
        else:
            xor_val <<= 1
            cur = cur.get_child(c)
    max_xor = max(max_xor, xor_val)
print(max_xor)