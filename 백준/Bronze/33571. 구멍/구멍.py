s = input()
answer = 0

for c in s:
    if c in ('A', 'a', 'b', 'D', 'd', 'e', 'g', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', '@'):
        answer += 1
    elif c == 'B':
        answer += 2

print(answer)