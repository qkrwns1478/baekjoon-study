import sys
input = sys.stdin.readline

def cut(w, x, y):
    if w == 0:
        return
    
    is_blue = 1
    is_white = 1
    for i in range(x, x+w):
        for j in range(y, y+w):
            if arr[i][j] == 1:
                is_white *= 0
            else:
                is_blue *= 0
                
    #print(w, x, y, is_blue)

    if is_blue:
        global cnt_b
        cnt_b += 1
        return
    
    if is_white:
        global cnt_w
        cnt_w += 1
        return
    
    else:
        cut(w//2, x, y)
        cut(w//2, x + w//2, y)
        cut(w//2, x, y + w//2)
        cut(w//2, x + w//2, y + w//2)
        

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))
    #print(*arr[i])

cnt_b = 0
cnt_w = 0
cut(n, 0, 0)

print(cnt_w)
print(cnt_b)