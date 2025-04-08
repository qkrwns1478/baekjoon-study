import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
ss = s.replace("pPAp", "*")
print(ss.count("*"))
