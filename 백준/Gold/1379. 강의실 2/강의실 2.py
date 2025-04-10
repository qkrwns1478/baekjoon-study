import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
queue = list()
lecture = list()
for _ in range(n):
    a, b, c = map(int, input().split())
    lecture.append((a, b, c))
lecture.sort(key=lambda x: (x[1], x[2]))
answer = [0] * (n+1)

idx = 1
heappush(queue, (lecture[0][2], idx))
answer[lecture[0][0]] = idx

for i in range(1, n):
    if queue[0][0] > lecture[i][1]:
        idx += 1
        answer[lecture[i][0]] = idx
        heappush(queue, (lecture[i][2], idx))
    else:
        _, t = heappop(queue)
        answer[lecture[i][0]] = t
        heappush(queue, (lecture[i][2], t))

print(len(queue))
print(*answer[1:], sep="\n")