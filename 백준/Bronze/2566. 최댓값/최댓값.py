arr = [[0 for _ in range(9)] for _ in range(9)]
max_val = 0
for i in range(9):
    arr[i] = list(map(int, input().split()))
    max_val = max(max_val, max(arr[i]))

print(max_val)

for i in range(9):
    for j in range(9):
        if arr[i][j] == max_val:
            print(i+1, j+1)
            break