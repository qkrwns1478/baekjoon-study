import sys
sys.setrecursionlimit(10**6)

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = list()

    pos = [0] * (n+1)
    for i in range(n):
        pos[inorder[i]] = i

    def solution(pre_l, pre_r, in_l, in_r):
        if pre_l > pre_r or in_l > in_r:
            return
        root = preorder[pre_l]
        mid = pos[root]
        left_size = mid - in_l
        
        solution(pre_l+1, pre_l+left_size, in_l, mid-1)
        solution(pre_l+left_size+1, pre_r, mid+1, in_r)
        postorder.append(root)

    solution(0, n-1, 0, n-1)
    print(*postorder)