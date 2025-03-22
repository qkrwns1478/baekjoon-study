n = int(input())
a, b = map(int, input().split())
chicken = 0
chicken += a//2
chicken += b
if chicken > n:
    chicken = n
print(chicken)