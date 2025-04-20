s = input()
ci = 0
cj = 0
for i in range(len(s)-2):
    if s[i:i+3] == "JOI": cj += 1
    elif s[i:i+3] == "IOI": ci += 1
print(cj)
print(ci)