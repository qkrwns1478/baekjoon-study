n = int(input())
dir = list(input())
for _ in range(1, n):
    new_dir = input()
    for j in range(len(dir)):
        if dir[j] != new_dir[j]:
            dir[j] = "?"
print(''.join(dir))