n = int(input())                                   #user input of type int
count = 0                                           #initialize count to 0 

for i in range(1,n+1):
    count = count + int(str("1"*i))                 #counting the sum of 1's series
print(count)


