class Hero:
    def __init__(self):
        self.HP = 20
        self.maxHP = 20
        self.ATT = 2
        self.W = 0
        self.DEF = 2
        self.A = 0
        self.LV = 1
        self.EXP = 0

    def gainExp(self, exp):
        maxEXP = self.LV * 5
        self.EXP += exp
        if self.EXP >= maxEXP:
            self.levelUp()

    def levelUp(self):
        self.LV += 1
        self.EXP = 0
        self.maxHP += 5
        self.HP = self.maxHP
        self.ATT += 2
        self.DEF += 2

    def getDamage(self, dmg):
        self.HP -= dmg

class Enemy:
    def __init__(self, x, y, name, ATT, DEF, HP, EXP):
        self.x = int(x) - 1
        self.y = int(y) - 1
        self.name = name
        self.ATT = int(ATT)
        self.DEF = int(DEF)
        self.HP = int(HP)
        self.maxHP = int(HP)
        self.EXP = int(EXP)

class Item:
    def __init__(self, x, y, T, S):
        self.x = int(x) - 1
        self.y = int(y) - 1
        self.T = T
        self.S = S

def getOIndex(S):
    if S == "HR": return 0
    elif S == "RE": return 1
    elif S == "CO": return 2
    elif S == "EX": return 3
    elif S == "DX": return 4
    elif S == "HU": return 5
    elif S == "CU": return 6

def getItem(x, y):
    global hero
    global equipO_cnt
    global equipO_flag
    for item in items:
        if item.x == x and item.y == y:
            if item.T == 'O':
                if equipO_cnt < 4:
                    osi = getOIndex(item.S)
                    if not equipO_flag[osi]:
                        equipO_flag[osi] = True
                        equipO_cnt += 1
            elif item.T == 'W':
                hero.W = int(item.S)
            elif item.T == 'A':
                hero.A = int(item.S)
            return

def battle(e, isBoss):
    global hero
    global equipO_flag
    isFirst = True
    while hero.HP > 0 and e.HP > 0:
        if isFirst and equipO_flag[2]:
            e.HP -= max(1, (hero.ATT + hero.W) * (3 if equipO_flag[4] else 2) - e.DEF)
        else:
            e.HP -= max(1, hero.ATT + hero.W - e.DEF)
            
        if e.HP > 0:
            if not (isFirst and isBoss and equipO_flag[5]):
                hero.HP -= max(1, e.ATT - (hero.DEF + hero.A))
        isFirst = False

def gameOver(S, T):
    global hero
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end='')
        print()
    print("Passed Turns :", T)
    print("LV :", hero.LV)
    print(f'HP : 0/{hero.maxHP}')
    print(f'ATT : {hero.ATT}+{hero.W}')
    print(f'DEF : {hero.DEF}+{hero.A}')
    print(f'EXP : {hero.EXP}/{hero.LV * 5}')
    print(f'YOU HAVE BEEN KILLED BY {S}..')
    exit()

def gameClear(T, x, y):
    global hero
    global posX
    global posY
    for i in range(n):
        for j in range(m):
            if i == posX and j == posY: print('@', end='')
            else: print(arr[i][j], end='')
        print()
    print("Passed Turns :", T)
    print("LV :", hero.LV)
    print(f'HP : {hero.HP}/{hero.maxHP}')
    print(f'ATT : {hero.ATT}+{hero.W}')
    print(f'DEF : {hero.DEF}+{hero.A}')
    print(f'EXP : {hero.EXP}/{hero.LV * 5}')
    print("YOU WIN!")
    exit()

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

hero = Hero()
posX, posY = 0, 0
startX, startY = 0, 0
equipO_cnt = 0
equipO_flag = [False, False, False, False, False, False, False]
k, l = 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == '@':
            posX = i
            posY = j
            startX = posX
            startY = posY
            arr[i][j] = '.'
        elif arr[i][j] == '&' or arr[i][j] == 'M':
            k += 1
        elif arr[i][j] == 'B':
            l += 1

cmd = input()

enemies = list()
items = list()

for _ in range(k):
    tmp = list(input().split())
    enemies.append(Enemy(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6]))
for _ in range(l):
    tmp = list(input().split())
    items.append(Item(tmp[0], tmp[1], tmp[2], tmp[3]))

turn = 0
for _ in range(len(cmd)):
    if cmd[turn] == 'U' and posX > 0 and arr[posX-1][posY] != '#': posX -= 1
    elif cmd[turn] == 'D' and posX < n-1 and arr[posX+1][posY] != '#': posX += 1
    elif cmd[turn] == 'L'and posY > 0 and arr[posX][posY-1] != '#': posY -= 1
    elif cmd[turn] == 'R' and posY < m-1 and arr[posX][posY+1] != '#': posY += 1
    
    turn += 1
    
    if arr[posX][posY] == 'B':
        getItem(posX, posY)
        arr[posX][posY] = '.'
        
    elif arr[posX][posY] == '^':
        if equipO_flag[4]: hero.getDamage(1)
        else: hero.getDamage(5)
        if hero.HP <= 0:
            if equipO_flag[1]:
                hero.HP = hero.maxHP
                posX = startX
                posY = startY
                equipO_flag[1] = False
                equipO_cnt -= 1
            else:
                gameOver("SPIKE TRAP", turn)
                
    elif arr[posX][posY] == '&' or arr[posX][posY] == 'M':
        for i in range(len(enemies)):
            if enemies[i].x == posX and enemies[i].y == posY:
                if arr[posX][posY] == 'M':
                    if equipO_flag[5]:
                        hero.HP = hero.maxHP
                    battle(enemies[i], True)
                else:
                    battle(enemies[i], False)
                
                if hero.HP <= 0:
                    if equipO_flag[1]:
                        hero.HP = hero.maxHP
                        enemies[i].HP = enemies[i].maxHP
                        posX = startX
                        posY = startY
                        equipO_flag[1] = False
                        equipO_cnt -= 1
                    else:
                        gameOver(enemies[i].name, turn)
                else:
                    is_boss = (arr[posX][posY] == 'M')
                    arr[posX][posY] = '.'
                    hero.gainExp(int(enemies[i].EXP * (1.2 if equipO_flag[3] else 1)))
                    if equipO_flag[0]:
                        hero.HP = min(hero.HP + 3, hero.maxHP)
                    if is_boss:
                        gameClear(turn, posX, posY)
                break

for i in range(n):
    for j in range(m):
        if i == posX and j == posY: print('@', end='')
        else: print(arr[i][j], end='')
    print()
print("Passed Turns :", turn)
print("LV :", hero.LV)
print(f'HP : {hero.HP}/{hero.maxHP}')
print(f'ATT : {hero.ATT}+{hero.W}')
print(f'DEF : {hero.DEF}+{hero.A}')
print(f'EXP : {hero.EXP}/{hero.LV * 5}')
print("Press any key to continue.")