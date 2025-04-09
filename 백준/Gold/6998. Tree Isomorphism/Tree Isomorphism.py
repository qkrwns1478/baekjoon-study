import sys
input = sys.stdin.readline

t = int(input())

def build_tree(st):
    stack = list()
    for s in st:
        if s == '#':
            children = list()
            while stack and stack[-1] != '(':
                children.append(stack.pop())
            stack.pop()
            children.sort()
            stack.append('(' + ''.join(children) + ')')
        else:
            stack.append('(')
        #print(stack)
    return stack[0]

for _ in range(t):
    tree1 = input().split()
    tree2 = input().split()
    t1 = build_tree(tree1)
    t2 = build_tree(tree2)
    
    if t1 == t2:
        print("The two trees are isomorphic.")
    else:
        print("The two trees are not isomorphic.")