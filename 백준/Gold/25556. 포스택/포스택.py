from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
stacks = [[0] for _ in range(4)]

def solution():
    for i in range(N):
        flag = False
        for j in range(4):
            if stacks[j][-1] < A[i]:
                stacks[j].append(A[i])
                flag = True
                break
        if not flag:
            return False
    return True

print("YES" if solution() else "NO")
