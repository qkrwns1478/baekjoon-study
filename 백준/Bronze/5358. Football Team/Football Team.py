while(True):
    try:
        name = list(input())
        for i in range(len(name)):
            if name[i] == 'i': name[i] = 'e'
            elif name[i] == 'e': name[i] = 'i'
            elif name[i] == 'I': name[i] = 'E'
            elif name[i] == 'E': name[i] = 'I'
        print(*name, sep='')
    except EOFError:
        break