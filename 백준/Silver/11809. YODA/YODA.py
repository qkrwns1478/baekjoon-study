def sol(s):
    res = ''.join(s).strip()
    return int(res) if res else "YODA"

N = list(input())
M = list(input())

for i in range(1, min(len(N), len(M)) + 1):
    if N[-i] < M[-i]: N[-i] = ''
    elif N[-i] > M[-i]: M[-i] = ''

print(sol(N))
print(sol(M))
