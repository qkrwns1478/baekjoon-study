import re

def shen(s):
    stack = list()
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)

        elif c == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()

        elif c == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

while True:
    s = input()

    if s == ".":
        break

    s = s.replace(" ","").replace(".","")
    s = re.sub(r"[A-Za-z]", "", s)

    print("yes" if shen(s) else "no")