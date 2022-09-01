num = int(input()) #list size
list_a = [] #creating a empty list

for i in range(0,num):
    context = input()
    list_a.append(context) #adding the elements to the list by using append
    
for i in range(num-1,0,-1): #printing all elements except first element
    print(list_a[i])
    
print(list_a[0]) #printing first element of list(that is before reversing)
    
    
