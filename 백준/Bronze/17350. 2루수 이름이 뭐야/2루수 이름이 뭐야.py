n = int(input())
cnt = 0
for _ in range(n):
    name = input()
    if name == "anj":
        cnt += 1
        break
if cnt > 0:
    print("뭐야;")
else:
    print("뭐야?")