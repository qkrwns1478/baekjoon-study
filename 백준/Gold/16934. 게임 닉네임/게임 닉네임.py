from collections import defaultdict
from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.child = dict()
    def add_child(self, child):
        self.child[child.value] = child

n = int(input())
d = defaultdict(int)
root = Node('')
for _ in range(n):
    s = input().strip()
    d[s] += 1
    
    flag = False
    tmp = list()
    cur = root
    for i in range(len(s)):
        if not flag:
            tmp.append(s[i])
        if s[i] not in cur.child:
            cur.add_child(Node(s[i]))
            if not flag:
                print(''.join(tmp))
                flag = True
        cur = cur.child[s[i]]
    
    if not flag:
        if d[s] > 1:
            tmp.append(str(d[s]))
        print(''.join(tmp))