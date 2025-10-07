from math import factorial as facto

ans = 0
print("n e")
print("- -----------")
for i in range(10):
    ans = 1 / facto(i) + ans
    if i == 0 or i == 1:
        print(f"{i} {int(ans)}")
    elif i == 2:
        print(f"{i} {ans:.1f}")
    else:
        print(f"{i} {ans:.9f}")