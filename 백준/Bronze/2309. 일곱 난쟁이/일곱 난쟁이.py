arr = list()
for _ in range(9):
    arr.append(int(input()))
total = sum(arr)

for i in range(9):
    for j in range(9):
        if i != j and total - (arr[i] + arr[j]) == 100:
            a, b = i, j

arrr = list()
for i in range(9):
    if i != a and i != b:
        arrr.append(arr[i])

arrr.sort()
for i in range(7):
    print(arrr[i])