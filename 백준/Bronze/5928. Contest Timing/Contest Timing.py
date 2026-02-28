d,h,m=map(int,input().split())
t=(d-11)*1440+h*60+m-671
if t<0:t=-1
print(t)