def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    arr = [100] * n
    for i in range(n):
        arr[i] -= progresses[i]

    for i in range(n):
        tmp = arr[i] // speeds[i]
        if arr[i] % speeds[i] > 0:
            tmp += 1
        arr[i] = tmp

    #print(arr)
    stack = list()
    for i in arr:
        if stack and i > stack[-1] and i > stack[0]:
            answer.append(len(stack))
            stack.clear()
        stack.append(i)

    if stack:
        answer.append(len(stack))

    return answer