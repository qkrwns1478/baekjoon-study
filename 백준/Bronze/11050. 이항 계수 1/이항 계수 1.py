from math import factorial as facto
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
print(facto(n) // (facto(n-k) * facto(k)))