s1=input()
s2=input()  
s3=input()
s4=input()

b1=int(input())
b2=int(input())     
b3=int(input())
b4=int(input()) 

slova = [s1, s2, s3, s4]
vrednosti = [b1, b2, b3, b4]
uredjene_vrednosti = [0, 0, 0, 0]

for i in range(4):
    if slova[i] == "A":        
        uredjene_vrednosti[0] = vrednosti[i]
    elif slova[i] == "B":        
        uredjene_vrednosti[1] = vrednosti[i]
    elif slova[i] == "C":        
        uredjene_vrednosti[2] = vrednosti[i]
    elif slova[i] == "D":        
        uredjene_vrednosti[3] = vrednosti[i]

if uredjene_vrednosti[0]>uredjene_vrednosti[1]>uredjene_vrednosti[2]>uredjene_vrednosti[3]:
    print(uredjene_vrednosti[0], uredjene_vrednosti[1], uredjene_vrednosti[2], uredjene_vrednosti[3])
else:
    print(uredjene_vrednosti[3]+uredjene_vrednosti[2]+uredjene_vrednosti[1]+uredjene_vrednosti[0])