n=int(input()) 
a, b=map(int,input().split())

t=a*a+2*a*b+b*b
p=a*a+b*b
nt=0
nn=0
no=0   
for i in range(1,n+1):
    ri=int(input())
    if ri==t:
        nt=nt+1 
       
    elif ri==p:
        nn=nn+1
    else:
        no=no+1
print(nt)
print(nn)
print(no)
