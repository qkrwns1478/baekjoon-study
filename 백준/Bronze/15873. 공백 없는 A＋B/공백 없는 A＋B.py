n = input()

if len(n) == 2:
    print(int(n[0]) + int(n[1]))

elif len(n) == 4:
    print(20)

else:
    if n[1] == "0":
        print(10 + int(n[2]))
    else:
        print(10 + int(n[0]))