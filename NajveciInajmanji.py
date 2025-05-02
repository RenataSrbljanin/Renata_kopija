# najveci broj

##n=int(input("koliko brojeva da uneses"))
##najveci=0
##najmanji=100
##for i in range(n):
##    broj=int(input("unesi broj"))
##    
##    if broj>najveci:
##        najveci=broj
## 
##    if broj<najmanji:
##        najmanji=broj
##        
##print(najveci)  
##print(najmanji)

# ako nemas odredjene granice za najvecu i najmanju vrednost

n=int(input("koliko brojeva da uneses: "))

for i in range(n):
    broj=int(input(f"unesi {i+1}. broj:"))
    if i==0:
       najveci=najmanji=broj
    else:
        if broj>najveci:
            najveci=broj
     
        elif broj<najmanji: #ovako je efikasnije sa elif
            najmanji=broj
        
print(najveci)  
print(najmanji)
