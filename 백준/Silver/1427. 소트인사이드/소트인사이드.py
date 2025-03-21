import sys
n = list(sys.stdin.readline().strip())
print(*sorted(n, reverse=True), sep='')