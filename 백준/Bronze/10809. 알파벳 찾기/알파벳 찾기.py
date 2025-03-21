S = input()
arr = [-1] * 26
for i in range(len(S)):
    c = S[i]
    if arr[ord(c)-97] == -1:
        arr[ord(c)-97] = i
print(*arr)