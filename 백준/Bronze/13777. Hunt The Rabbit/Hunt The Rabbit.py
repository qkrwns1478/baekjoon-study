while True:
    n = int(input())

    if n == 0:
        break
    pl = 1
    pr = 50

    while pl <= pr:
        mid = (pl + pr)//2

        if mid == n:
            print(mid)
            break
        elif n > mid:
            print(mid, end=" ")
            pl = mid+1
        else:
            print(mid, end=" ")
            pr = mid-1