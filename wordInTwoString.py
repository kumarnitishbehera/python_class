str1=input("Please enter the string one :")
str2=input("please enter string two: ")

word=input("Please enter the word you want to search")

if(word in str1)and (word in str2):
    print("The word was found in both the statement")
elif(word in str1) or (word in str2):
    print("Word was found in one statement")
else:
    print("The word was not found !!!!!")
