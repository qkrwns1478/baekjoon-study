from math import comb

N, M, K = map(int, input().split())

def P(x):
    return 1 - comb(N - M, x) / comb(N, x)

for x in range(1, K+1):
    print("{:.10f}".format(P(x)))
