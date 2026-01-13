S = input()
answer = ''
stack1 = list()
stack2 = list()
is_tag = False

for c in S:
    if c == '<':
        is_tag = True
        if stack1:
            answer += ''.join(stack1[::-1])
            stack1 = list()
    elif c == '>':
        is_tag = False
        answer += f"<{''.join(stack2)}>"
        stack2 = list()
    elif is_tag:
        stack2.append(c)
    elif c == ' ':
        answer += ''.join(stack1[::-1]) + ' '
        stack1 = list()
    else:
        stack1.append(c)
if stack1:
    answer += ''.join(stack1[::-1])
print(answer)
