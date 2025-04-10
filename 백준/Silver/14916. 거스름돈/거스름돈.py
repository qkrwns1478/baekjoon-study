n = int(input())
flag = False
for i in range(n//5, -1, -1):
    answer = i
    j = n - 5*i
    if j % 2 == 0 and i * 5 + (j // 2) * 2 == n:
        answer += j // 2
        flag = True
        break
print(answer if flag else -1)