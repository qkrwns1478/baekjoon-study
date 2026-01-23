N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit()

answer = 0
while len(boxes) > 0:
    tmp = set()
    idx = 0
    for crane in cranes:
        if not boxes:
            break
        flag = False
        while idx < len(boxes):
            if crane >= boxes[idx]:
                tmp.add(idx)
                idx += 1
                flag = True
                break
            idx += 1
        if not flag:
            break
    new_boxes = list()
    for i in range(len(boxes)):
        if i not in tmp:
            new_boxes.append(boxes[i])
    boxes = new_boxes
    answer += 1
print(answer)
