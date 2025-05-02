
p=int(input())
t=int(input())
l=int(input())

rp=int(input())
rt=int(input())
rl=int(input())

zp=int(input())
zt=int(input())
zl=int(input())

def u_l(l,t,p):
    return l+t*100+p*20*100
    
l_trazeno=u_l(l,t,p)

r_ponuda=u_l(rl,rt,rp)
z_ponuda=u_l(zl,zt,zp)

def ispisi_pobednika(r,z):
    if r>z:
        print("ROM")
    else: print("ZEK")

print(l_trazeno)
ispisi_pobednika(r_ponuda,z_ponuda)
print((abs(r_ponuda-z_ponuda)//2000)+1)
# delta_u_listicima = abs(r_ponuda-z_ponuda)
# def pretvori_u_najmanje_potrebno_poluga(listica):
#     print("Modulo je "+str(listica%2000))
#     poluga=listica//2000
#     if listica%2000>=0:
#         poluga=poluga+1
#     return poluga    

# print(pretvori_u_najmanje_potrebno_poluga(delta_u_listicima))