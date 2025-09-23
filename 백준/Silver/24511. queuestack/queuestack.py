from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))

queue = deque()
for i in range(n):
    if A[i] == 0:
        queue.append(B[i])

answer = []
for i in range(m):
    queue.appendleft(C[i])
    answer.append(queue.pop())

print(*answer)