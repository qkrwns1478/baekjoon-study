from math import comb
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
print(comb(n-1,k-1))