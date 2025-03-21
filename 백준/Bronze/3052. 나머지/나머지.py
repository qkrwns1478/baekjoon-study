stack = list()
for _ in range(10):
    stack.append(int(input()))
for i in range(10):
    stack[i] %= 42
ss = set(stack)
print(len(ss))