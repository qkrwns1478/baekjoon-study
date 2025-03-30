import sys
input = sys.stdin.readline

arr = list(input().strip().split("-"))
#print(arr)

def sejun(s):
    sum = 0
    tmp = s.split("+")
    for i in tmp:
        sum += int(i)
    return sum

answer = 0
for i in range(len(arr)):
    tmp = sejun(arr[i])
    #print(tmp)
    if i == 0:
        answer += tmp
    else:
        answer -= tmp
    #print(answer)

print(answer)