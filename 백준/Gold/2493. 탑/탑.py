import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
stack = list()
answer = [0] * n

for i in range(n):
    while stack and t[stack[-1]] < t[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1] + 1
            
    stack.append(i)

print(*answer)