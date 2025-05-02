s=input()

igrac1=0
igrac2=0
for i in range(0, len(s), 4):
    if s[i]>s[i+2]:
        igrac1=igrac1+1
    else:
        igrac2=igrac2+1
        
if igrac1>igrac2:
    print("ime1")
else:
    print("ime2")

print(igrac1, igrac2)
