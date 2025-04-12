a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
feeA = a
if t >= 30: feeA += 21 * (t-30) * x
feeB = b
if t >= 45: feeB += 21 * (t-45) * y
print(feeA, feeB)