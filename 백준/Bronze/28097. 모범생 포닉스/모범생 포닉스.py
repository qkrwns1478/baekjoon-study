n = int(input())
arr = list(map(int, input().split()))
time = sum(arr) + (8*(n-1))
d, t = time // 24, time % 24
print(d, t)