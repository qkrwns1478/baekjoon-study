h = input()
n = input()
cnt = 0
for i in range(len(h)-len(n)+1):
    if h[i:i+len(n)] == n:
        cnt += 1
print(cnt)