n = int(input())
for _ in range(n):
    v, i = 0, 0
    q = input()
    for j in range(len(q)):
        if q[j] == 'O':
            i += 1
            v += i
        else:
            i = 0
    print(v)