import sys
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

def matrix_mul(A, B):
    AB = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                AB[i][j] += A[i][k] * B[k][j]
            AB[i][j] %= 1000

    return AB

def matrix_pow(A, k):
    if k == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A
    if k == 0:
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    mid = k // 2
    half = matrix_pow(A, mid)
    if k % 2 == 0:
        return matrix_mul(half, half)
    else:
        return matrix_mul(matrix_mul(half, half), A)

power = matrix_pow(arr, b)
for i in range(n):
    print(*power[i])