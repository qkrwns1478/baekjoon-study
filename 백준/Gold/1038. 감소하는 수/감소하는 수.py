from itertools import combinations as comb

n = int(input())
d = list(str(i) for i in range(10))
arr = list()
for i in range(1, 11):
    for c in comb(d, i):
        s = ''.join(sorted(c, reverse=True))
        if s == '0' or s[0] != '0':
            arr.append(int(s))
arr.sort()

if n >= len(arr):
    print(-1)
else:
    print(arr[n])