x = int(input())
n = int(input())
answer = 0
for _ in range(n):
    a, b = map(int,input().split())
    answer += a * b
print("Yes" if answer == x else "No")