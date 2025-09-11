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

def count_mkdir(N, is_counting: bool = False):
    res = 0
    for _ in range(N):
        inputs = input().strip()
        arr = list(inputs.split('/'))
        arr[0] = "root"
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
                    if is_counting:
                        res += 1
                    new_node = Node(arr[j], cur)
                    cur.add_child(new_node)
                    cur = new_node
            
    return res

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().strip().split())
    root = Node("root", None)
    tree = Tree(root)
    
    count_mkdir(n)
    answer = count_mkdir(m, True)
    
    print(f"Case #{case}: {answer}")