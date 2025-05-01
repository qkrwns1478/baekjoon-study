arr = list()
for _ in range(5):
    arr.append(int(input()))
a = min(arr[0], arr[1], arr[2])
b = min(arr[3], arr[4])
print(a+b-50)