stabla=[]
odrezano=0
# 1<n<1000 000,  1<m<2000 000 000, 0<h<1000 000 000
n, m = map(int, input().split())

stabla=list(map(int, input().split()))
stabla.sort()

max=stabla[-1]
min=stabla[0]
height=(max-min)//2
for i in range(len(stabla)):
    if stabla[i]<height:
        odrezano=odrezano+height-min
        print(odrezano)
        
        
print(stabla)