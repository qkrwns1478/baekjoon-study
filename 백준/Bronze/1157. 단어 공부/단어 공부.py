word = input()
d = dict()
for c in word:
    if c.upper() not in d:
        d[c.upper()] = 1
    else:
        d[c.upper()] += 1

max_val = 0
max_c = ''
for c in d:
    if d[c] > max_val:
        max_val = d[c]
        max_c = c
    elif d[c] == max_val:
        max_c = '?'
print(max_c)