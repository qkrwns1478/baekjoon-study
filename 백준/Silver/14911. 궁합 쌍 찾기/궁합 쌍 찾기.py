arr = list(map(int, input().split()))
n = int(input())

arr.sort()
visited = set()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == n and (arr[i], arr[j]) not in visited:
            print(arr[i], arr[j])
            visited.add((arr[i], arr[j]))

print(len(visited))
