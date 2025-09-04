s = input()
arr = [0] * 26
for c in s:
    arr[ord(c) - 97] += 1
print(*arr)