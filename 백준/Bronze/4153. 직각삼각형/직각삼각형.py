import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c = arr[0], arr[1], arr[2]
    if a == 0 and b == 0 and c == 0:
         break

    print("right" if a**2 + b**2 == c**2 else "wrong")