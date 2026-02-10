from math import factorial as facto

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = facto(M) // (facto(N) * facto(M-N))
    print(ans)
