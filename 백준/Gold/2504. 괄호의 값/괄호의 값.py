import sys
input = sys.stdin.readline

s = input()
s = s.replace("()", "2").replace("[]", "3")

stack = list()
tmp = 0
answer = 0

for c in s:
    #print(*stack)
    try:
        if c == '(' or c == '[':
            stack.append(c)

        elif c == '2' or c == '3':
            stack.append(int(c))

        elif c == ')':
            if not stack or '(' not in stack or stack[-1] == '[':
                answer = -1
                break
            else:
                tmp = 0
                
                while type(stack[-1]) == int:
                    tmp += stack.pop()

                if not stack or '(' not in stack or stack[-1] == '[':
                    answer = -1
                    break

                stack.pop()
                tmp *= 2
                stack.append(tmp)

        elif c == ']':
            if not stack or '[' not in stack or stack[-1] == '(':
                answer = -1
                break
            else:
                tmp = 0
                
                while type(stack[-1]) == int:
                    tmp += stack.pop()

                if not stack or '[' not in stack or stack[-1] == '(':
                    answer = -1
                    break

                stack.pop()
                tmp *= 3
                stack.append(tmp)
    except:
        pass

while stack and answer > -1:
    try:
        answer += stack.pop()
    except:
        answer = -1
        break
print(0 if answer == -1 else answer)