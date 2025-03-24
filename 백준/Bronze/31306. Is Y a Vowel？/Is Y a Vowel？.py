s = input()
yes, no = 0, 0
for c in s:
    if c in ("a", "e", "i", "o", "u"):
        yes += 1
        no += 1
    elif c == "y":
        no += 1
print(yes, no)