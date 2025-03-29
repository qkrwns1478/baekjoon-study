import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '1':
            maze[i][j] = 1

visited = set()
queue = deque()
queue.append((0,0))
#answer = 0

while queue:
    v = queue.popleft()
    #print(v, v in visited)
    
    if v not in visited:
        visited.add(v)
        x, y = v[0], v[1]
        #flag = False

        if x > 0 and maze[x-1][y] > 0 and (x-1, y) not in visited and (x-1, y) not in queue:
            #answer += 1
            #flag = True
            maze[x-1][y] += maze[x][y]
            queue.append((x-1, y))
            
        if x < n-1 and maze[x+1][y] > 0 and (x+1,y) not in visited and (x+1, y) not in queue:
            #answer += 1
            #flag = True
            maze[x+1][y] += maze[x][y]
            queue.append((x+1, y))
            
        if y > 0 and maze[x][y-1] > 0 and (x,y-1) not in visited and (x, y-1) not in queue:
            #answer += 1
            #flag = True
            maze[x][y-1] += maze[x][y]
            queue.append((x, y-1))
            
        if y < m-1 and maze[x][y+1] > 0 and (x,y+1) not in visited and (x, y+1) not in queue:
            #answer += 1
            #flag = True
            maze[x][y+1] += maze[x][y]
            queue.append((x, y+1))
    
    #if not flag:
    #    answer -= 1
    
#print(answer)
print(maze[n-1][m-1])
