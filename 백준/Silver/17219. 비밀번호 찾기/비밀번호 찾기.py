import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwd = dict()
for _ in range(n):
    site, pw = input().split()
    pwd[site] = pw
for _ in range(m):
    print(pwd[input().strip()])