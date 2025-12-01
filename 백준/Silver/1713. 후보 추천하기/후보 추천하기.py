N = int(input())
M = int(input())
arr = list(map(int, input().split()))

likes = [0] * 101
period = [0] * 101
frames = set()

for i in range(M):
    if arr[i] in frames:
        likes[arr[i]] += 1
        continue
    if len(frames) == N:
        tmp = [(j, likes[j], period[j]) for j in frames]
        tmp.sort(key=lambda x:(x[1], x[2]))
        bye = tmp[0][0]
        frames.remove(bye)
        likes[bye] = 0
        period[bye] = 0
    frames.add(arr[i])
    likes[arr[i]] += 1
    period[arr[i]] = i

print(*sorted(list(frames)))
