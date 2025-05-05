n, h, v = map(int, input().split())
a = n - h
b = n - v
print(max(h*v,h*b,a*v,a*b) * 4)