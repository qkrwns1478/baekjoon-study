import sys
input = sys.stdin.readline

s = input().strip()
ans = int(s == s[::-1])
print(ans)