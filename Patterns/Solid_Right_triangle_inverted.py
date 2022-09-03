row  = int(input())

for i in range(0,row):
    for j in range(1,i+1):
        print(' ',end=' ')
    for j in range(row,i,-1):  
      print("*",end=" ")
    print()
