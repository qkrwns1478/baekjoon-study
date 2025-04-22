t = int(input())
n = int(input())
f = list(map(int, input().split()))

name = "Padaeng_i"
mood = "Happy" if t <= sum(f) else "Cry"
print(name, mood)