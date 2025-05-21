from math import factorial as facto
t = int(input())
for _ in range(t):
    n = int(input())
    print(facto(n) % 10)