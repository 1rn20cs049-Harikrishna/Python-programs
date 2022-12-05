num = int(input()) #list size
list_a = [] #creating a empty list
list_b = []
for i in range(0,num):
    context = input()
    list_a.append(context) #adding the elements to the list by using append

for i in range(len(list_a)-1,-1,-1):
    list_b.append(list_a[i])
print(list_b)
    


# OR 
#print(num[::-1]) # it will reverse the list
    
    
