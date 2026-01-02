from collections import deque

K = int(input())
A = deque()
for _ in range(6):
    a, b = map(int, input().split())
    A.append((a, b))

def get_pattern(queue):
    while queue[0][0] != 3 or queue[1][0] != 1:
        queue.rotate(1)
    p = ''
    for i in range(6):
        p += str(queue[i][0])
    if p == '313142' or p == '314231':
        if p == '314231':
            queue.rotate(2)
        return 0
    elif p == '314142':
        return 1
    elif p == '314242':
        return 2
    else:
        return 3

def get_area(W, L, w, l):
    return A[W][1] * A[L][1] - A[w][1] * A[l][1]

pattern = get_pattern(A)
if pattern == 0:
    area = get_area(5, 4, 1, 2)
elif pattern == 1:
    area = get_area(5, 0, 3, 2)
elif pattern == 2:
    area = get_area(1, 0, 3, 4)
else:
    area = get_area(2, 1, 5, 4)
print(area * K)
