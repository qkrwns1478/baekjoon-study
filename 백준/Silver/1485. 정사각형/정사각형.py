from math import *

def get_angle(p1, p2, p3):
    try:
        v21 = p1[0] - p2[0], p1[1] - p2[1]
        v23 = p3[0] - p2[0], p3[1] - p2[1]
        dot_product = v21[0] * v23[0] + v21[1] * v23[1]
        mag_21 = sqrt(v21[0] ** 2 + v21[1] ** 2)
        mag_23 = sqrt(v23[0] ** 2 + v23[1] ** 2)
        cos_theta = dot_product / (mag_21 * mag_23)
        angle = acos(cos_theta)
        return degrees(angle)
    except:
        return 0

def get_dist(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def check_square(arr):
    p1, p2, p3, p4 = arr
    line12 = get_dist(p1, p2)
    line13 = get_dist(p1, p3)
    line24 = get_dist(p2, p4)
    line34 = get_dist(p3, p4)
    if not (line12 == line13 == line24 == line34):
        return 0
    angle213 = get_angle(p2, p1, p3)
    angle243 = get_angle(p2, p4, p3)
    if not (angle213 == angle243 == 90.0):
        return 0
    return 1

T = int(input())
for _ in range(T):
    arr = list()
    for _ in range(4):
        x, y = map(int, input().split())
        arr.append((x, y))
    arr.sort()
    print(check_square(arr))
