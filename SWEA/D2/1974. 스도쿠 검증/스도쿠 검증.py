T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    def solution():
        nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(9):
            # 행
            if set(arr[i]) != nums:
                return 0
            # 열
            tmp = set()
            for j in range(9):
                tmp.add(arr[j][i])
            if tmp != nums:
                return 0
            # 부분행렬
            subset = set()
            for j in range(3):
                for k in range(3):
                    subset.add(arr[(i//3)*3 + j][(i%3)*3 + k])
            if subset != nums:
                return 0
        return 1
    
    print(f"#{t} {solution()}")