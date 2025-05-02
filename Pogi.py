
n=int(input())
k=int(input())
x=int(input())
ui_list=[]
ui_list_skracena=[]
koliko=0
for i in range(k):
    ui_list.append(int(input()))
ui_set = set(ui_list)
if x in ui_set:
    print("DA")
    

else:
    print("NE")
    print(0)


for i in range(len(ui_list)):
        if i==0: ui_list_skracena.append(ui_list[i])
        elif ui_list[i] in ui_list_skracena:
            continue
        else:
            ui_list_skracena.append(ui_list[i])
            if ui_list[i]==x:
                    print(len(ui_list_skracena))
    
print(len(ui_list_skracena))
print(*ui_list_skracena)
