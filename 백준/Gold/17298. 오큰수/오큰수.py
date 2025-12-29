from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

# NGE = [[] for _ in range(N)]
# for i in range(N-1, 0, -1):
#     for j in range(i-1, -1, -1):
#         if A[j] < A[i]:
#             NGE[j].append(A[i])
# for i in range(N):
#     print(NGE[i][-1] if NGE[i] else -1, end=' ')

NGE = [-1 for _ in range(N)]
stack = [0]
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)
