zbroj=0
brojevi=[]
n=int(input())
for i in range(n):
    a=int(input())
    brojevi.append(a)
    if a>9 and a<100:
        zbroj=zbroj+a//10+a%10
    elif a>999 and a<10000:
        moguci=[]
        b=a//1000+a%1000
        c=a//100+a%100
        d=a//10+a%10
        moguci.append(b)
        moguci.append(c)
        moguci.append(d)
        zbroj=zbroj+max(moguci)
    else:
        zbroj=zbroj+a
    
print(zbroj)   
    
