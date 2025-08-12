import sys
input = sys.stdin.readline
n = int(input())
log = set()
cnt = 0
for _ in range(n):
    s = input().strip()
    if s != "ENTER" and s not in log:
        log.add(s)
    elif s == "ENTER":
        cnt += len(log)
        log.clear()
if log: cnt += len(log)
print(cnt)
