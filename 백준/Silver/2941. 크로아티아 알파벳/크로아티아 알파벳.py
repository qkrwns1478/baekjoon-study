import sys
input = sys.stdin.readline

s = input().strip()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in arr:
    s = s.replace(c, '*')
print(len(s))