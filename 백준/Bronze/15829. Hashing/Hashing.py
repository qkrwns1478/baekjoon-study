import sys
input = sys.stdin.readline

l = int(input())
s = input()
r = 31
M = 1234567891

sh = 0
for i in range(l):
    sh += (ord(s[i]) -96) * (r ** i)
H = sh % M
print(H)