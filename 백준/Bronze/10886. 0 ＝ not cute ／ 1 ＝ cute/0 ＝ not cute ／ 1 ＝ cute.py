n = int(input())
ones = 0
zeros = 0
for _ in range(n):
    x = int(input())
    if x == 0:
        zeros += 1
    else:
        ones += 1
if ones > zeros:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")