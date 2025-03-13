mi = 0
mv = 0
for i in range(1, 10):
    n = int(input())
    if n > mv:
        mi = i
        mv = n
print(f"{mv}\n{mi}")