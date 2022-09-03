n = int(input())                                                       #input

for i in range(0,n):
    for  j in range(0,n):
        if i == (n-1)  or  j == (n - 1) or j == n - i -1  :             #conditions to print
              print("*",end=" ")                                        #printing the star in same line ..with spaces
        else:
             print(' ',end=' ')                                         #providing space in line between stars
    print()                                                              #To move to next column
        
        
