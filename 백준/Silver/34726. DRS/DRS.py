from sys import stdin
input = stdin.readline

N, T = map(int, input().split())
A = list()

for _ in range(N):
    inputs = input().split()
    Di = inputs[0]
    ti = int(inputs[1])
    A.append([Di, ti])
for i in range(1, N):
    A[i][1]  = (A[i-1][1] - A[i][1]) % T
A.sort(key=lambda x: x[1])

answer = list()
for i in range(N-1):
    if 0 < A[i+1][1] - A[i][1] <= 1000:
        answer.append(A[i][0])

if 0 < T - A[N-1][1] <= 1000:
    answer.append(A[N-1][0])

answer.sort()
if len(answer) > 0:
    print(*answer)
else:
    print(-1)
