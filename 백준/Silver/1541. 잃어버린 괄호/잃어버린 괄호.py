import sys
input = sys.stdin.readline

s = input().strip().split('-')

for i in range(len(s)):
    if s[i].isdigit():
        s[i] = int(s[i])
    else:
        tmp = list(map(int, s[i].split('+')))
        s[i] = sum(tmp)

answer = s[0]
for i in range(1, len(s)):
    answer -= s[i]
print(answer)