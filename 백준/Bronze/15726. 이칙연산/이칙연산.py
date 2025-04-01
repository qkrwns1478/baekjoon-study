a, b, c = map(int, input().split())
d = a * b / c
e = a / b * c
print(int(max(d,e)))