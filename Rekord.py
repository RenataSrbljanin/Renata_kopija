wr, ol, pr = 72.28, 71.53, 66.18
n=int(input())
zaispis=[]

def popunjavanje_rezultata(duljina):
    if(duljina>wr):
        zaispis.append("WR")
    elif(duljina>ol):   
        zaispis.append("OR")
    elif(duljina>pr):
        zaispis.append("PB")
    else:
        zaispis.append(duljina)
        
for i in range(n):
    popunjavanje_rezultata(float(input()))
for i in range(n):
    print(zaispis[i])
    
