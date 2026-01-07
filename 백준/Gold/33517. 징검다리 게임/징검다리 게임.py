from bisect import bisect_left
from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
K = input().strip()
alive = True
pos = 0

if 'J' not in K:
    print("NO")
    exit()

JAD = {'J': [], 'A': [], 'D': []}
for i in range(M):
    JAD[K[i]].append(i)

has_bear = False
for i in range(N):
    if A[i] > 0:
        has_bear = True
        break
if has_bear and not JAD['A']:
    print("NO")
    exit()

has_mine = False
for i in range(N):
    if A[i] == -1:
        has_mine = True
        break
if has_mine and not JAD['D']:
    print("NO")
    exit()

def find_target(char, cur, cnt):
    jad = JAD[char]
    L = len(jad)
    if L == 0:
        return float('inf')

    start_pos = bisect_left(jad, cur % M)
    rem = L - start_pos
    if cnt <= rem:
        return (cur // M) * M + jad[start_pos + cnt - 1]
    else:
        nxt_rem = cnt - rem
        nxt_start = ((cur // M) + 1) * M
        return nxt_start + ((nxt_rem - 1) // L) * M + jad[(nxt_rem - 1) % L]

for i in range(N-1):
    if A[i+1] == -1:
        d_pos = find_target('D', pos, 1)
        j_pos = find_target('J', pos, 1)
        a_pos = find_target('A', pos, 1)
        if j_pos < d_pos or a_pos < d_pos:
            alive = False
            break
        pos = d_pos + 1
    elif A[i+1] > 0:
        kill_pos = find_target('A', pos, A[i+1])
        j_pos = find_target('J', pos, 1)
        if j_pos < kill_pos:
            alive = False
            break
        pos = kill_pos + 1
    j_pos = find_target('J', pos, 1)
    pos = j_pos + 1

print("대상혁" if pos > 10**100 else ("YES" if alive else "NO"))
