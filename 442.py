n=input()
for i in range(len(n)-1,1, -1):

    if int(n[i-2])+int(n[i-1])+int(n[i])==10:
        print(int(n[i-2]),int(n[i-1]),int(n[i]),sep=" ")
        break
