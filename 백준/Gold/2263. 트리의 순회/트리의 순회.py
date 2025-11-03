import sys
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
answer = list()

pos = [0] * (n+1)
for i in range(n):
    pos[inorder[i]] = i

def solution(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return
    root = postorder[post_r]
    mid = pos[root]
    left_size = mid - in_l
    
    answer.append(root)
    solution(in_l, mid-1, post_l, post_l+left_size-1)
    solution(mid+1, in_r, post_l+left_size, post_r-1)

solution(0, n-1, 0, n-1)
print(*answer)