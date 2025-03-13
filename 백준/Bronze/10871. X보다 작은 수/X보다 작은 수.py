n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = list()
for i in arr:
    if i < x:
        ans.append(str(i))
print(" ".join(ans))