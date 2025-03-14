a = int(input())
b = int(input())
c = int(input())
abc = str(a*b*c)
d = {i: 0 for i in range(10)}
for i in range(len(abc)):
    d[int(abc[i])] += 1
for i in range(10):
    print(d[i])