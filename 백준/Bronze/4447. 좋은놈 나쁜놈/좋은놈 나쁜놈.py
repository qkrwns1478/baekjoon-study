n = int(input())
for _ in range(n):
    h = input()
    g = h.lower().count("g")
    b = h.lower().count("b")

    if g > b:
        answer = "GOOD"
    elif g < b:
        answer = "A BADDY"
    else:
        answer = "NEUTRAL"

    print(f"{h} is {answer}")
