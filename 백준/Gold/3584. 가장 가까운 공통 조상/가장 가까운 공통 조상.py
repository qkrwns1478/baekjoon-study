from collections import defaultdict

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = dict()
    def add_child(self, new_value):
        child = Node(new_value, self)
        self.child[new_value] = child

def test(arrA, arrB):
    for i in range(len(arrA)):
        for j in range(len(arrB)):
            if arrA[i] == arrB[j]:
                return arrA[i]
    return arrA[len(arrA)-1]

T = int(input())
for _ in range(T):
    n = int(input())
    nodes = defaultdict(Node)
    for _ in range(n-1):
        a, b = map(int, input().split())
        if a in nodes:
            nodeA = nodes[a]
        else:
            nodeA = Node(a, None)
            nodes[a] = nodeA
        if b in nodes:
            nodeB = nodes[b]
        else:
            nodeB = Node(b, None)
            nodes[b] = nodeB
        nodeA.add_child(nodeB)
        nodeB.parent = nodeA

    a, b = map(int, input().split())
    cur = nodes[a]
    parentsA = [cur]
    while cur.parent != None:
        parentsA.append(cur.parent)
        cur = cur.parent
    cur = nodes[b]
    parentsB = [cur]
    while cur.parent != None:
        parentsB.append(cur.parent)
        cur = cur.parent
    '''
    for i in range(len(parentsA)):
        print(parentsA[i].value, end=' ')
    print()
    for i in range(len(parentsB)):
        print(parentsB[i].value, end=' ')
    print()
    '''
    answer = test(parentsA, parentsB)
    print(answer.value)