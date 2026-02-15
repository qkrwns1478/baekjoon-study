N = int(input())
A = [0] * 365
for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S-1, E):
        A[i] += 1

R, C = 0, 0
answer = 0
for i in range(365):
    if A[i] != 0:
        R = max(R, A[i])
        C += 1
    else:
        answer += R * C
        R, C = 0, 0
answer += R * C
print(answer)
