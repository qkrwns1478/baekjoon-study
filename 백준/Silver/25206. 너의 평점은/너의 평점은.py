import sys
input = sys.stdin.readline

dict_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
total = 0.0
a_sum = 0.0
for _ in range(20):
    _, a, b = input().split()
    if b != 'P':
        a_sum += float(a)
        total += float(a) * dict_score[b]
ans = total / a_sum
print("{:.6f}".format(ans))