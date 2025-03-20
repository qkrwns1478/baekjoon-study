def cut(h):
    tmp = 0
    for i in arr:
        if i > h:
            tmp += i - h
    return tmp

n, m = map(int, input().split())
arr = list(map(int, input().split()))

pl, pr = 0, max(arr)
answer = 0

while True:
    if pl > pr:
        break
    mid = (pl + pr) // 2
    if cut(mid) >= m:
        answer = mid
        pl = mid + 1
    else:
        pr = mid - 1
print(answer)