def kitty():
    for _ in range(15):
        arr = list(input().split())
        if 'w' in arr:
            return "chunbae"
        elif 'b' in arr:
            return "nabi"
        elif 'g' in arr:
            return "yeongcheol"

print(kitty())