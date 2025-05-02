##s=input()
##m=input()
##
##h=0
##min=0
##
##for i in range(len(s)):
##    if s[i]=="1":
##     #   print(len(s)-i-1)
##        h=h+2**(len(s)-i-1)
##for i in range(len(m)):
##    if m[i]=="1":
##       # print(len(m)-i-1)
##        min=min+2**(len(m)-i-1)
##
##print(h, min, sep=" ")  
# s=s[::-1]

s=input()
m=input()

s=s[::-1]
m=m[::-1]

h=0
min=0

for i in range(len(s)):
    if s[i]=="1":    
           h=h+2**(i)
for i in range(len(m)):
    if m[i]=="1":
           min=min+2**(i)

print(h, min, sep=" ")  
