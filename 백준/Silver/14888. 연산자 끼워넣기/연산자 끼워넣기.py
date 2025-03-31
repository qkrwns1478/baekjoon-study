import sys
input = sys.stdin.readline
from itertools import permutations

def calc(a, b, mode):
    if mode == 0:
        return a + b
    elif mode == 1:
        return a - b
    elif mode == 2:
        return a * b
    else:
        if a > 0:
            return a // b
        else:
            return -(-a // b)

n = int(input().strip())
A = list(map(int, input().strip().split())) # 숫자
B = list(map(int, input().strip().split())) # 기호

max_val = float("-inf")
min_val = float("inf")

tmp = list()
for i in range(4):
    for _ in range(B[i]):
        tmp.append(i)

pmt = permutations(tmp)
for p in pmt:
    answer = A[0]
    idx = 1
    for i in p:
        answer = calc(answer, A[idx], i)
        idx += 1
    if max_val < answer:
        max_val = answer
    if min_val > answer:
        min_val = answer
            
print(max_val)
print(min_val)