n  = int(input())                            #input

for i in range (0,n):
    for j in range(0,n):
        if j == (n-1) or i == j or i == 0:  #conditions for required pattern
            print('*',end=" ")
        else:
            print(' ',end=" ")              #providing space bettwen star's
    print()                                 #to go to next line
    
    
       
