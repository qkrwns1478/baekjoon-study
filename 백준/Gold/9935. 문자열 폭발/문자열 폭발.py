import sys
input = sys.stdin.readline

s = input().strip()
b = input().strip()

stack = list()
bomb = list()

for c in s:
    if c not in b:
        if bomb:
            stack.extend(bomb)
            bomb.clear()
            
        stack.append(c)
        
    else:
        bomb.append(c)
        if ''.join(bomb[-len(b):]) == b:
            for _ in range(len(b)):
                bomb.pop()
                
while bomb:
    if ''.join(bomb[-len(b):]) == b:
        for _ in range(len(b)):
            bomb.pop()
    else:
        break
                
if bomb:
    stack.extend(bomb)

print(''.join(stack) or "FRULA")