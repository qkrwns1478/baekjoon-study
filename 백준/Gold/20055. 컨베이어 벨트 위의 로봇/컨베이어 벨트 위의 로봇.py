from collections import deque

N, K = map(int, input().split())
a = list(map(int, input().split()))
A = deque()
for i in range(2 * N):
    A.append([a[i], False])

step = 0
zero = 0

def decrease(pos):
    A[pos][0] -= 1
    if A[pos][0] == 0:
        global zero
        zero += 1

while True:
    step += 1
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    A.rotate(1)
    A[N-1][1] = False
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(N-2, -1, -1):
        if A[i][1] and not A[i+1][1] and A[i+1][0] > 0:
            A[i][1] = False
            if i != N-2:
                A[i+1][1] = True
            decrease(i+1)
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if A[0][0] > 0 and not A[0][1]:
        A[0][1] = True
        decrease(0)
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if zero >= K:
        break

print(step)