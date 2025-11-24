N = int(input())
G = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
X = int(input())

A = [True] * N
a = N
INF = 10 ** 9
answer = 0

def game(cur_G, cur_A, cur_a, cur_nights):
    global answer
    if cur_a == 1 and cur_A[X]:
        answer = max(answer, cur_nights)
        return

    if cur_a % 2 == 1:
        dead = cur_G.index(max(cur_G))
        if dead == X:
            answer = max(answer, cur_nights)
            return
        cur_A[dead] = False
        tmp = cur_G[dead]
        cur_G[dead] = -INF
        game(cur_G, cur_A, cur_a - 1, cur_nights)
        cur_A[dead] = True
        cur_G[dead] = tmp
    else:
        for i in range(N):
            if i == X or not A[i]:
                continue
            cur_A[i] = False
            tmp = cur_G[i]
            cur_G[i] = -INF
            for j in range(N):
                cur_G[j] += R[i][j]
            game(cur_G, cur_A, cur_a - 1, cur_nights + 1)
            cur_A[i] = True
            for j in range(N):
                cur_G[j] -= R[i][j]
            cur_G[i] = tmp

game(G, A, a, 0)
print(answer)