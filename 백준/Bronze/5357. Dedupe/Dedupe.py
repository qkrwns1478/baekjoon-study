n = int(input())
for _ in range(n):
    x = input()
    prev = None
    answer = ""
    for c in x:
        if prev != c:
            answer += c
            prev = c
    print(answer)