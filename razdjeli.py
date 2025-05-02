##n = int(input())
##
##m=0
##for a in range(1, n-2):
##    for b in range(1,n-a):
##        for c in range(1, n-a-b+1):
##            if a+b+c==n and a<=b and b<=c:
##                m=m+1
##print(m)
            


##n = int(input())
##
##m=0
##for a in range(1, n-2):
##    for b in range(a,n-a):
##        for c in range(b,n):
##            if a+b+c==n  #and a<=b and b<=c:
##                m=m+1
##print(m)    


n = int(input())
m=0
for a in range(1, n//3+1):
    for b in range(a,n//2+1):
        c=n-a-b
        if c>=b:      
            m=m+1
print(m)    
