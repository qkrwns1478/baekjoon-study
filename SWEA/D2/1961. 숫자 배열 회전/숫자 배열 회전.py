T = int(input())
for t in range(1, T+1):
    N = int(input())
    a0 = [list(map(int, input().split())) for _ in range(N)]
    ans = [[] for _ in range(N)]

    a1 = [row[::-1] for row in zip(*a0)]
    a2 = [row[::-1] for row in a0[::-1]]
    a3 = [row[::-1] for row in zip(*a2)]

    print(f"#{t}")
    for i in range(N):
        ans[i].append(''.join(str(num) for num in a1[i]))
        ans[i].append(''.join(str(num) for num in a2[i]))
        ans[i].append(''.join(str(num) for num in a3[i]))
        print(*ans[i])