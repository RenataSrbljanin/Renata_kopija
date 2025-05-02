def prebaciUminute(s,m):
   m= s*60+m
   if m>=24*60:
       m=m-24*60
   return m

def h_m(m):
   h=int(m/60)
   m=m-h*60
   return (h,m)
