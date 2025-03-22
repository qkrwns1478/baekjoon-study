t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n%h or h
    room = '{0:02d}'.format(n//h + 1 if n%h else n//h)
    print(str(floor) + room)