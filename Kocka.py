a=int(input())
b=int(input())
kombinacije=[[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]], # nijedan
             [[1,0],[2,2],[3,2],[4,4],[5,4],[6,4]], #samo kutovi
             [[1,0],[2,0],[3,0],[4,0],[5,0],[6,2]], #samo rubovi
             [[1,1],[2,0],[3,1],[4,0],[5,1],[6,0]], #samo sredina
             [[1,0],[2,2],[3,2],[4,4],[5,4],[6,6]], #kutovi i rubovi
             [[1,1],[2,2],[3,3],[4,4],[5,5],[6,4]], #kutovi i sredina
             [[1,1],[2,0],[3,1],[4,0],[5,1],[6,2]], #sredina i rubovi
             [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]] #sredina,rubovi,kutovi

for i in range(8):
   # print(kombinacije[i][a-1][1]) 
      if kombinacije[i][a-1][1] == b:  
        print(i+1, end=" ")