import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cloth = dict()
    
    for _ in range(n):
        _, b = input().split()
        if b not in cloth:
            cloth[b] = 1
        cloth[b] += 1

    answer = 1
    for c in cloth:
        answer *= cloth[c]
        
    print(answer - 1)