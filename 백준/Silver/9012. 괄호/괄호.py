import sys
from collections import deque

def vps(word):
    stack = deque()
    for i in range(len(word)):
        if word[i] == "(":
            stack.append("(")
        elif word[i] == ")":
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True

t = int(sys.stdin.readline())
for _ in range(t):
    word = sys.stdin.readline()
    print("YES" if vps(word) else "NO")