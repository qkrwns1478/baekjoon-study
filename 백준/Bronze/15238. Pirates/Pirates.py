from collections import defaultdict
n = int(input())
s = input()
dict = defaultdict(int)
for i in range(n):
    dict[s[i]] += 1

ans = ''
wer = 0
for c in dict:
    if dict[c] > wer:
        ans = c
        wer = dict[c]
print(ans, wer)