s = input()
if 'x' in s:
    a, b = s.split('x')
    is_minus_a = False
    if len(a) > 0 and a[0] == '-':
        a = a[1:]
        is_minus_a = True
    if a == '':
        a = '1'
    a = int(a) // 2
    is_minus_b = False
    if len(b) > 0 and b[0] == '-':
        b = b[1:]
        is_minus_b = True
    if b == '':
        b = '0'
    b = int(b)

    da = str(a) + 'xx' if a not in (0, 1) else ('xx' if a == 1 else '')
    db = str(b) + 'x' if b not in (0, 1) else ('x' if b == 1 else '')
    print(f"{'-' if is_minus_a else ''}{da}{'-' if is_minus_b else '+'}{db}{'+' if db != '' else ''}W")
elif s == '0':
    print('W')
else:
    db = str(s) if int(s) not in (1, -1) else ('' if s == '1' else '-')
    print(db + "x+W")
