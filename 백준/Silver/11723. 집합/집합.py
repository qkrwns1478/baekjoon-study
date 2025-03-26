import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    query = input().split()

    if query[0] == "add":
        s.add(int(query[1]))

    elif query[0] == "remove":
        try:
            s.remove(int(query[1]))
        except:
            pass

    elif query[0] == "check":
        print(1 if int(query[1]) in s else 0)

    elif query[0] == "toggle":
        if int(query[1]) in s:
            s.remove(int(query[1]))
        else:
            s.add(int(query[1]))

    elif query[0] == "all":
        s = set(range(1,21))

    elif query[0] == "empty":
        s = set()