


##def prebaciUminute(s,m):
##   m= s*60+m
##   if m>=24*60:
##       m=m-24*60
##   return m

##def h_m(m):
##   h=int(m/60)
##   m=m-h*60
##   return (h,m)

def krajFilma(x,h,m):
    kf=h*60+m+x
    kfs=(kf//60)%24
    kfm=kf%60
    print(kfs, kfm)

def pogledano(lista):
    pocetak_filma=lista[0]*60+lista[1]
    pocetak_gledanja=lista[2]*60+lista[3]
    if pocetak_gledanja<pocetak_filma:
        pocetak_gledanja=pocetak_gledanja+1440
    kraj_gledanja=lista[4]*60+lista[5]
    if kraj_gledanja<pocetak_gledanja:
        kraj_gledanja=kraj_gledanja+1440 

    for i in range(pocetak_gledanja-pocetak_filma,kraj_gledanja-pocetak_filma):
        odgledano.add(i)


x=int(input())
n=int(input())

odgledano=set()

##for i in range(n):
##    pfs,pfm=map(int, input().split())
##    print(h_m(prebaciUminute(pfs, pfm)+x))
##    pgs,pgm=map(int, input().split())
## #   print(h_m(prebaciUminute(pgs, pgm)+x))
##    kgs,kgm=map(int, input().split())
  #  print(h_m(prebaciUminute(kgs, kgm)+x))


for i in range(n):
    pfs,pfm=map(int, input().split()) 
    pgs,pgm=map(int, input().split()) 
    kgs,kgm=map(int, input().split())

    lista=[pfs,pfm,pgs,pgm,kgs,kgm]
    krajFilma(x,pfs,pfm)
    pogledano(lista)

print(len(odgledano))
# set ne prima duplikate!!!




##def pogledano():
##    pocetak_filma=pfs*60+pfm
##    pocetak_gledanja=pgs*60+pfm
##    if pocetak_gledanja<pocetak_filma:
##        pocetak_gledanja=pocetak_gledanja+1440
##    kraj_gledanja=kgs*60+kgm
##    if kraj_gledanja<pocetak_gledanja:
##        kraj_gledanja=kraj_gledanja+1440 
##
##    for i in range(pocetak_gledanja-pocetak_filma,kraj_gledanja-pocetak_filma):
##        odgledano.add(i)
## #   print(ogledano)
