import matematika
import math
import random
from datetime import datetime
import os
import statistics

brojevi=[4,5,6,7,8,99,55,77,95]
print()
print(brojevi)
print("Prosek je:",statistics.mean(brojevi)) # prosek
print("Medijan je:",statistics.median(brojevi)) # medijan
print("Standardna devijacija:",statistics.stdev(brojevi))# standardna devijacija

print()
# print(os.getcwdb())
# print(os.listdir(), sep="\n")

# print()
# trenutno = datetime.now()
# print(trenutno)
# print(trenutno.date())
# print(trenutno.strftime("%d.%m.%Y. %H:%M"))
# print()
# print(matematika.kvadrat(5))

# print(int(math.pow(2,3)), math.pi)
# print(round(math.pow(2,3),3))

# n=float(input("Unesite decimalni broj:"))
# print(math.floor(n))

# r=float(input("Unesite radijus:"))
# povrsina = round(r**2*math.pi,2)
# opseg = round(2*r*math.pi,2)

# print(povrsina, opseg)

# b=int(input("Unesite bazu:"))
# ex=float(input("Unesite eksponent:"))
# eksponent = round(math.pow(b,ex),2)

# print(eksponent)

# a=int(input("Unesite prvu stranicu:"))
# b=int(input("Unesite drugu stravicu:"))

# print(matematika.hypotenuza(a,b))

print("Random broj je",random.randint(1,101))
# print(random.random())
print("Random odabrana boja je",random.choice(["crveno","plavo","zuto"]))

#print(random.randint(1,100))
lista=[]
for i in range(1,101):
    if i%5==0:
        lista.append(i)

print(lista)
print(random.choice(lista))


print()
broj=random.choice(range(5,10001,5))
print(broj)
print()
