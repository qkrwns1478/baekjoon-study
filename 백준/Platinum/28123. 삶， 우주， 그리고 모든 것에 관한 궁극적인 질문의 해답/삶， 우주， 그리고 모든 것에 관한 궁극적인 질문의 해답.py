import sys
input = sys.stdin.readline

arr = [0, 1, 2, 2, 3, 3, 3, 3, 4, 4]
n, k, x = map(int, input().split())

answer = (n+1 - arr[x]) - 3*(k-1)
if x in (4, 8, 9):
    answer += 1

print(answer)