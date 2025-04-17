import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    b = bin(n)[2:]
    for i in range(len(b)):
        if b[len(b)-i-1] == "1":
            print(i, end = " ")