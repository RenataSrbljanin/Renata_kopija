

pocetak=90*60

deltari=0
deltaru=0

n=int(input())

for i in range(n):
    m, s=map(int,input().split(":"))
    if i%2==0:
      deltari=deltari+m*60+s-30
    
    else:
      deltaru=deltaru+m*60+s-30
  
    hri=pocetak-deltari
    hru=pocetak-deltaru

mhri = hri//60
if mhri<10:textmhri ="0"+str(mhri)
else:textmhri =str(mhri)
shri = hri%60
if shri<10:textshri ="0"+str(shri)
else:textshri =str(shri)

mhru = hru//60
if mhru<10:textmhru ="0"+str(mhru)
else:textmhru =str(mhru)
shru = hru%60
if shru<10:textshru ="0"+str(shru)
else:textshru =str(shru)

print(textmhri,textshri,sep=":")
print(textmhru,textshru,sep=":")




