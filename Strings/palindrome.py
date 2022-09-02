n  = input()                     #user input

n = n.lower()                    #converting the user input to lower or uppercase 
#n = n.upper()

N = n == n[::-1]                 #reversing the user input and checking the user inputed string and revsered string same or different
if N:
    print("True")                # displaying suitable sentence
else:
    print("False")
 
