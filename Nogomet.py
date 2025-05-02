golovi=[]

hr=int(input())
for i in range(hr):
    ime, minuta=map(str, input().split())
    golovi.append([int(minuta), ime, "hr"])

    
br=int(input())
for i in range(br):
    ime, minuta=map(str, input().split())
    golovi.append([int(minuta), ime, "br"])

#print(golovi)
golovi.sort() # ovo je klucno, jer sortira po prvim clanovima koji su integeri
h=0
b=0
for i in range(len(golovi)):
    if golovi[i][2]=="hr":
        h=h+1
    elif golovi[i][2]=="br":
        b=b+1
    
    print(f"{h}:{b} {golovi[i][1]}")
