arr = [0] * 30
for _ in range(28):
    i = int(input())
    arr[i-1] += 1
for i in range(30):
    if arr[i] == 0:
        print(i+1)