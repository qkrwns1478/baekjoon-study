import sys
input = sys.stdin.readline

while True:
    data = input().strip()
    if int(data[0]) == 0:
        break
    
    idx = data.find(" ")

    n = int(data[:idx])
    arr = list(map(int, data[idx+1:].split()))

    stack = list()
    answer = 0

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            tmp = stack.pop()
            h = arr[tmp]
            if not stack:
                w = i
            else:
                w = i - stack[-1] - 1
            answer = max(answer, h*w)
            
        stack.append(i)

    while stack:
        tmp = stack.pop()
        h = arr[tmp]
        if not stack:
            w = n
        else:
            w = n - stack[-1] - 1
        answer = max(answer, h*w)

    print(answer)