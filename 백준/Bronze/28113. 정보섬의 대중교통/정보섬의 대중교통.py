n, a, b = map(int, input().split())
s = b if n <= b else 10**6+1
print("Bus" if a < s else "Subway" if a > s else "Anything")