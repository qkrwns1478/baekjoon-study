p, m = map(int, input().split())
players = list()
for _ in range(p):
    l, n = input().split()
    players.append((int(l), n))
rooms = list()

def find_room(x):
    if len(rooms) == 0:
        return -1
    for i in range(len(rooms)):
        if rooms[i][0] == m:
            continue
        if rooms[i][1] - 10 <= players[x][0] <= rooms[i][1] + 10:
            return i
    return -1

for i in range(p):
    room = find_room(i)
    if room == -1:
        rooms.append([1, players[i][0], {i}])
    else:
        rooms[room][0] += 1
        rooms[room][2].add(i)

for i in range(len(rooms)):
    if rooms[i][0] == m:
        print("Started!")
    else:
        print("Waiting!")
    tmp = list()
    for player in rooms[i][2]:
        tmp.append((players[player][0], players[player][1]))
    tmp.sort(key=lambda x: x[1])
    for j in range(len(tmp)):
        print(tmp[j][0], tmp[j][1])
