f=int(input())
s=int(input())
p=int(input())
pf=f*12*20
ps=s*12

print(p+pf+ps)

##h=int(input())
##m=int(input())
##s=int(input())
##
##u=s+m*60+h*60*60
##
##print(u)


##m=int(input())
##h=m//60+m%60
##
##print(h)


s=int(input())


h=s//(60*60)
m=(s-h*60*60)//60
o=s-h*60*60-m*60

print(h,m,o)
