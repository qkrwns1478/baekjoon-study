from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, N-1
res = float('inf')
ans = [0, 0, 0]

# while left < right:
#     L, R = arr[left], arr[right]
#     lleft, rright = left+1, right-1
#     while lleft <= rright:
#         mid = (lleft + rright) // 2
#         cur = L + R + arr[mid]
#         if res > abs(cur):
#             res = abs(cur)
#             ans = [L, arr[mid], R]
#         if cur < 0:
#             lleft = mid + 1
#         elif cur > 0:
#             rright = mid - 1
#         else:
#             lleft = rright + 1
#     if L + R < 0:
#         left += 1
#     else:
#         right -= 1
# print(*ans)

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        tmp = arr[i] + arr[left] + arr[right]
        if res > abs(tmp):
            res = abs(tmp)
            ans = [arr[i], arr[left], arr[right]]
        if tmp == 0:
            print(*ans)
            exit()
        elif tmp > 0:
            right -= 1
        else:
            left += 1

print(*ans)