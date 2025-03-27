import sys
input = sys.stdin.readline

n = int(input())
card1 = set(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

for i in range(m):
    if card2[i] in card1:
        card2[i] = 1
    else:
        card2[i] = 0

print(*card2)