n=int(input())
kaovi=[]
def nadjiRazliku(k):
    s=str(k)
    l=list(s)
    lsorted=l.copy()
    lsorted.sort()
    lreversed=lsorted.copy()
    lreversed.reverse()
    # print(l)
    # print(lsorted)
    a=int(''.join(lsorted))
   # print(lreversed)
    b=int(''.join(lreversed))
   # print(a,b)
    return b-a
def kolikoPuta(k):  
    x=nadjiRazliku(k)
    for i in range(7):
        if x==6174:
            return i+1
        elif x<1000 or x>9999:
            return 'NE'
        else:
            x=nadjiRazliku(x)    
def kolikoPuta_x(k):
    x=nadjiRazliku(k)
    i=1
    while x!=6174 and x>999 and x<10000:
        x=nadjiRazliku(x)
        i=i+1
    if x==6174:
        return i
    else:
        return "NE"
for i in range(n):
    k=int(input())
    kaovi.append(k)
#    print(nadjiRazliku(k))
# print()
# print(kaovi)
for k in kaovi:
    print(kolikoPuta_x(k))
    