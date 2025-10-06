from math import gcd

def get_fraction(a, b):
    g = gcd(a, b)
    return (a//g, b//g)

base = 20358520
p12 = 188
p11 = 1472
p10 = 14664
p9 = 165984
p8 = 205976
p7 = 39780
p6 = 39780
p5 = 282060
p4 = 732160
p3 = 2532816
p2 = 9730740
p1 = 6612900

pp = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
for p in pp:
    a, b = get_fraction(p, base)
    print(f'{a}/{b}')