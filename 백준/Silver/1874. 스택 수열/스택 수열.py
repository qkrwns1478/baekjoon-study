n = int(input())
stack = list()
answer = list()
flag = True

cur = 1
for _ in range(n):
    i = int(input())
    while cur <= i:
        stack.append(cur)
        answer.append('+')
        cur += 1
    if stack and stack[-1] == i:
        stack.pop()
        answer.append('-')
    else:
        flag = False
        break

if not flag:
    print('NO')
else:
    for c in answer:
        print(c)