firstword = input()
secondword = input()

list_1 = list(firstword)  #converting the string to character array
list_2 = list(secondword)

list_1.sort() #sorting the character array
list_2.sort()

flag = 0
if len(list_1) == len(list_2):   #checking both the strings for same length
    for i in range(len(list_1)):
        if list_1[i] == list_2[i]: 
            flag = 1
            continue
        else:
            break
if flag ==1 :
    print("Given string is Anagram")
else:
    print("Not a Anagram")
