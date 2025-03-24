n = int(input())
s = input()
ss = ""
for c in s:
    if c.isupper():
        ss += c.lower()
    else:
        ss += c.upper()
print(ss)