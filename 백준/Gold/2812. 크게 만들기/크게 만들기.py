import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().strip()

stack = list()
cnt = k

for c in s:
    while stack and stack[-1] < c and cnt:
        stack.pop()
        cnt -= 1

    stack.append(c)

while len(stack) > n-k:
    stack.pop()
    
print(''.join(stack))