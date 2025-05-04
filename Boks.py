s=[]
for i in range(3):
    s.append(input())
index_glavnog=int(input())-1
if s.count("A") >=2:
    print("A")
elif s.count("B") >=2:  
    print("B")
elif s[index_glavnog] == "N":
    print("N")
else: 
    if s[index_glavnog] == "A":
        print("A")
    else:
        print("B")