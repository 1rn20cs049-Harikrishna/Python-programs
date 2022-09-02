sentence = input()                                #user input
vowel_string = 'aeiouAEIOU'                       #to check the upper and lower case vowels

for char in sentence:
    if char in vowel_string:                      #checking the vowels in inputed sentence
        sentence = sentence.replace(char,'')      #replacing nothing inplace of vowels
print(sentence)                                   #output without vowels of actual sentence

