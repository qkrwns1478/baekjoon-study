N=int(input());A=[list(map(int,input().split()))for _ in range(N)];dp=[1]*N;A.sort()
for i in range(1,N):
    for j in range(i):
        if A[j][1]<A[i][1]:dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))