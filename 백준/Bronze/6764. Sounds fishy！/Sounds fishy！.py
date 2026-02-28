A=[int(input()) for _ in range(4)]
a,b,c,d=A
s="No Fish"
if a<b<c<d:s="Fish Rising"
if a>b>c>d:s="Fish Diving"
if a==b==c==d:s="Fish At Constant Depth"
print(s)