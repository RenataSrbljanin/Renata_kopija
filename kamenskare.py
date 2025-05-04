n=int(input())
m,s=0,0
# K>S S>P P>K
for i in range(n):
    a,b=input().split(" ")
    if (a=='K' and b=='S') or (a=='S' and b=='P') or (a=='P' and b=='K'):
        m=m+1
    elif (a=='S' and b=='K') or (a=='P' and b=='S') or (a=='K' and b=='P'):
        s=s+1
if m>=s:
    print("Magda")
else:
    print("Stjepan")