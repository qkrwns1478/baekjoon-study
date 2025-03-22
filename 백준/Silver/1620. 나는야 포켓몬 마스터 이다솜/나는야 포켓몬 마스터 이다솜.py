import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokedex = ["Missing no."]
pokedex_num = {"Missing no.": 0}

for i in range(1, n+1):
    name = input().strip()
    pokedex.append(name)
    pokedex_num[name] = i

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        q = int(q)
        print(pokedex[q])
    else:
        print(pokedex_num[q])