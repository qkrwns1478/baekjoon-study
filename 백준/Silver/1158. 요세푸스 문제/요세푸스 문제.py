import sys

n, k = map(int, sys.stdin.readline().split())
result = list()
stack = list(range(1, n+1))

idx = 0
while stack:
    idx = (idx+k-1) % len(stack)
    result.append(stack.pop(idx))

print("<", end="")
print(", ".join(map(str, result)), end="")
print(">")