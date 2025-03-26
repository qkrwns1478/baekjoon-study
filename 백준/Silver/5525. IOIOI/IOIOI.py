import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

t = "I"
for _ in range(n):
    t += "OI"

answer = 0
for i in range(m - len(t)+1):
    if s[i:i+len(t)] == t:
        answer += 1

print(answer)