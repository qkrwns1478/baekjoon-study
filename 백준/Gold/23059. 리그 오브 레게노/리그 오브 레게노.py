from collections import defaultdict
from heapq import heappush, heappop

n = int(input())
d = defaultdict(int)
items = defaultdict(list)
all_items = set()

for _ in range(n):
    a, b = input().split()
    items[a].append(b)
    d[b] += 1
    all_items.add(a)
    all_items.add(b)

queue = list()
for item in all_items:
    if d[item] == 0:
        heappush(queue, item)

result = list()
tmp = list()
while queue:
    item = heappop(queue)
    result.append(item)
    for next_item in items[item]:
        d[next_item] -= 1
        if d[next_item] == 0:
            heappush(tmp, next_item)
    if not queue:
        if not tmp:
            break
        queue = tmp
        tmp = list()

if len(result) == len(all_items):
    for item in result:
        print(item)
else:
    print(-1)