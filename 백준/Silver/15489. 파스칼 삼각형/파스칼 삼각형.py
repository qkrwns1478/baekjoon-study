from math import comb

r, c, w = map(int, input().split())
answer = 0
for i in range(w):
    for j in range(i+1):
        answer += comb(r-1+i, c-1+j)
print(answer)