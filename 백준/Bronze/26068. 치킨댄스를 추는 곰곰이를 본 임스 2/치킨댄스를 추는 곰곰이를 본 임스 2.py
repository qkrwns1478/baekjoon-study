n = int(input())
answer = 0
for _ in range(n):
    s = input()
    s = int(s[2:])
    if s <= 90:
        answer += 1
print(answer)