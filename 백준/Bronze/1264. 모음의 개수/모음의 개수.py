while True:
    s = input()
    if s == "#":
        break

    cnt = 0
    vowels = ["A", "E", "I", "O", "U"]
    s = s.upper()
    
    for v in vowels:
        cnt += s.count(v)
    print(cnt)