import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def post(arr):
    left = list()
    right = list()
    
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    #print(left, right)
            
    if left:
        post(left)
        
    if right:
        post(right)
        
    print(arr[0])

arr = list()

while True:
    try:
        arr.append(int(input().strip()))
    except:
        break

post(arr)