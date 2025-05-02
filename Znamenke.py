# ako zelimo iz nekog broja dobiti znamenke: delimo sa deset, a ostatak je druga znamenka

# 254/100 = 2
# 45/10 = 4
# 2/10 = 2

#  2746 / 10 =274 ostatak 6
#  274 / 10 = 27 ostatak 4
#  27,1 / 10 = 2
#  2 / 10 = 0

# radimo while dok ne dobijemo 0;  n=n//10

n=int(input("unesi broj cije znamenke zelis da pronadjes: "))
brojac=0
while n>0:
    print(n%10)
    brojac=brojac+1
    n=n//10
    print("Broj n je sada ",n)
print("Ukupno znamenki je ", brojac)
