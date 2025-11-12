from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.child = dict()
        self.is_end = False
    def add_child(self, child):
        self.child[child.value] = child

C, N = map(int, input().split())

root = Node('')
for _ in range(C):
    color = input().strip()
    cur = root
    for c in color:
        if c not in cur.child:
            cur.add_child(Node(c))
        cur = cur.child[c]
    cur.is_end = True

names = set()
for _ in range(N):
    names.add(input().strip())

Q = int(input())
for _ in range(Q):
    team = input().strip()
    cur = root
    flag = False
    i = 0
    while i < len(team):
        c = team[i]
        if c not in cur.child:
            break
        cur = cur.child[c]
        i += 1
        if cur.is_end:
            rem = team[i:]
            if rem in names:
                flag = True
                print("Yes")
                break
    
    if not flag:
        print("No")