import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    x, r = map(int, input().split())
    arr.append((x-r, 1)) # (
    arr.append((x+r, 0)) # )

arr.sort(key = lambda x: (x[0], x[1]))
#print(arr)

stack = list()
answer = 1

for a, b in arr:
    if b == 1: # (
        stack.append((a, "("))

    elif b == 0: # )
        ww = 0
        while stack:
            tmp = stack.pop()
            if tmp[1] == "(":
                w = a - tmp[0]
                answer += 2 if w == ww else 1
                stack.append((w, "○"))
                break
            
            elif tmp[1] == "○":
                ww += tmp[0]

print(answer)