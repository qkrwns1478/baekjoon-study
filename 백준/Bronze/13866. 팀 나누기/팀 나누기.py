from itertools import permutations as pmts
answer = float("inf")
arr = list(map(int, input().split()))
pmt = pmts(arr, 4)
for p in pmt:
    a, b, c, d = list(p)
    answer = min(answer, abs((a+b)-(c+d)))
print(answer)