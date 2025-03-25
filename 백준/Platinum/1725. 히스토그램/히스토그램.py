import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    arr.append(int(input()))

stack = list()
answer = 0

for i in range(n):
    #print(stack)
    while stack and stack[-1][1] > arr[i]:
        h = stack.pop()[1]
        w = i if not stack else i - stack[-1][0] -1
        answer = max(answer, h*w)

    stack.append((i, arr[i]))

while stack:
    h = stack.pop()[1]
    w = n if not stack else n - stack[-1][0] -1
    answer = max(answer, h*w)

print(answer)