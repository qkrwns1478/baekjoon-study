n, k = map(int, input().split())
arr = list(tuple(map(int, input().split())) for _ in range(n))
from itertools import combinations as comb

def get_dist(xi, yi, xj, yj):
    return abs(xi - xj) + abs(yi - yj)

min_dist = float("inf")

cmb = comb(arr, k)
for c in cmb: # c에는 k개의 대피소 리스트가 저장됨
    dist = list()
    for hx, hy in arr:
        if (hx, hy) not in c:
            tmp = list()
            for sx, sy in c:
                tmp.append(get_dist(hx, hy, sx, sy))
            dist.append(min(tmp))
    min_dist = min(min_dist, max(dist))
print(min_dist)