n=int(input()) 
prethodnik=0
ukupno_vrijeme=0

for i in range(n):
    a=int(input())
    
    if i%2!=0:
        ukupno_vrijeme=ukupno_vrijeme+a-prethodnik
        
    prethodnik=a
    
if n%2==0:
    print(ukupno_vrijeme)   
else:
    print("UPALJENO")


