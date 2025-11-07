from itertools import product as prod
s = input()
cl = ["A", "C", "G", "T"]

def check(s):
    for c in cl:
        if c not in s:
            print(c)
            return True
    return False
        
def solution(s):
    for i in range(1, len(s)):
        pdt = prod(cl, repeat=i)
        for p in pdt:
            pj = ''.join(p)
            if pj not in s:
                print(pj)
                return

if not check(s):
    solution(s)