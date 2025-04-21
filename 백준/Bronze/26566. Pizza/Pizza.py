from math import pi
t = int(input())
for _ in range(t):
    a1, p1 = map(int, input().split()) # pizza slice
    r1, p2 = map(int, input().split()) # circular pizza
    c1 = pi * r1 * r1
    d1 = a1 / p1
    d2 = c1 / p2
    print("Whole pizza" if d1 < d2 else "Slice of pizza")